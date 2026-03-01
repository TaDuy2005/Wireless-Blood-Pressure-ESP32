#include "BluetoothSerial.h"
#include <Arduino.h>
#include "HX711.h"

//only work if bluetooth is enabled on device
#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif

//Bluetooth
BluetoothSerial SerialBT;
int input;

//Timer
hw_timer_t *timer_Pressure = NULL;
bool read_pressure = false;
int time_sec = 30;

// HX711 and pressure sensor
const int LOADCELL_DOUT_PIN = 27;
const int LOADCELL_SCK_PIN = 26;
HX711 pressure;
float value;

//Pump
const int pump_pin = 19;
bool pumpState = false; // false means OFF

//Valve
const int valve_pin = 17;
bool valveState = false; // false means OFF

void IRAM_ATTR Pressure_reading_check()
{
  read_pressure = true;
}

void do_Pressure_reading(){
  valveState = true; 
  digitalWrite(valve_pin, valveState ? HIGH : LOW);
  pumpState = true; 
  digitalWrite(pump_pin, pumpState ? HIGH : LOW);
  while(true){
    value = pressure.get_units(5);
    Serial.println(value);
    delay(7000);
    value = 31;
    if(value>30){
      value = pressure.get_units(5);
      SerialBT.println(value);
      valveState = false; 
      digitalWrite(valve_pin, valveState ? HIGH : LOW);
      pumpState = false; 
      digitalWrite(pump_pin, pumpState ? HIGH : LOW);
      read_pressure = false;
      break;
    }
  }
}

void setup() {
  Serial.begin(115200);

  //bluetooth
  SerialBT.begin("ESP32test"); //Bluetooth device name

  //sensor
  pressure.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);
  pressure.set_scale(100);
  pressure.tare(); 

  //pump/valve
  pinMode(pump_pin, OUTPUT); // Set pump pin as an output
  pinMode(valve_pin, OUTPUT); // Set valve pin as an output

  // Initial states
  digitalWrite(pump_pin, LOW); // Turn off pump initially
  digitalWrite(valve_pin, LOW); // Turn off valves initially

  //timer
  timer_Pressure = timerBegin(0, 80, true);
  timerStop(timer_Pressure);
  SerialBT.println("Enter '1' to turn pump on/off");
  SerialBT.println("Enter '2' to turn valve on/off");
  SerialBT.println("Enter '3' to start measurements");
  SerialBT.println("Enter '4' for emergency shutoff");
}

void loop() {
  if (SerialBT.available()) {
    input = SerialBT.parseInt();
    switch(input){
      case 0:
        break;
      case 1:
      //pump functionality
        pumpState = !pumpState; // Toggle pump state
        digitalWrite(pump_pin, pumpState ? HIGH : LOW);
        SerialBT.print("Pump turned ");
        SerialBT.println(pumpState ? "ON." : "OFF.");
        break;
      case 2:
      //valve functionality
        valveState = !valveState; // Toggle valve state
        digitalWrite(valve_pin, valveState ? HIGH : LOW);
        SerialBT.print("Valves turned ");
        SerialBT.println(valveState ? "ON." : "OFF.");
        break;
      case 3:
        //start device and timer
        SerialBT.println("Starting device");
        SerialBT.println("Taking initial reading...");
        do_Pressure_reading();
        //timerStart(timer_Pressure);
        timerStart(timer_Pressure);
        timerAttachInterrupt(timer_Pressure, &Pressure_reading_check, true);
        timerAlarmWrite(timer_Pressure, time_sec*1000*1000, true);
        timerAlarmEnable(timer_Pressure);
        break;
      case 4:
        //emergency stop
        //in the future could use interrupts
        valveState = false; 
        digitalWrite(valve_pin, valveState ? HIGH : LOW);
        pumpState = false; 
        digitalWrite(pump_pin, pumpState ? HIGH : LOW);
        timerStop(timer_Pressure);
        break;
      default:
        Serial.println("Please enter a valid command");
      }
  }
  input=0;
  delay(20);
  if(read_pressure){
     do_Pressure_reading();
  }
}
