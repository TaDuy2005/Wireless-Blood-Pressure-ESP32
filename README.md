# Wireless Blood Pressure Device (ESP32)

Engineering Technology Innovation Project  
Swinburne University of Technology  
Semester 2, 2024  

---

## 📌 Project Overview

This project redesigns a conventional blood pressure monitor into a **wireless embedded triage device** intended for emergency department environments.

The system automatically inflates a cuff, monitors pressure using a transducer and ADC, and transmits data wirelessly via Bluetooth.

The objective is to reduce triage delays by enabling automated and repeatable blood pressure monitoring.

---

## 🧠 Motivation

Emergency departments frequently experience congestion, leading to delays in vital sign collection.

This device aims to:

- Automate blood pressure measurement
- Reduce manual nurse intervention
- Enable wireless data transmission
- Provide repeatable time-based monitoring cycles
- Support future integration into hospital IoT systems

---

## ⚙️ System Architecture

### 🔹 Hardware Architecture

The system consists of:

- **ESP32** – Main controller and wireless communication
- **Pressure Sensor** – Measures cuff pressure
- **HX711 (24-bit ADC)** – Signal conditioning for pressure sensor
- **Air Compressor** – Cuff inflation
- **Air Valve** – Controlled deflation
- **Transistor Switching Circuits** – Drive inductive loads
- **Flyback Diodes** – Protect against back-EMF
- **5V External Supply** – Power source

See schematic:

[schematic.png](hardware/Schematic.png)


The compressor and valve are driven using transistor-based low-side switching with flyback diode protection to prevent inductive voltage spikes.

---

### 🔹 Software Architecture

Firmware developed using:

- Arduino framework for ESP32
- BluetoothSerial communication
- Hardware timer interrupts
- Threshold-based control logic

### Operating Sequence

1. Compressor and valve activate
2. Cuff inflates
3. Pressure monitored via HX711
4. When pressure threshold is reached:
   - Final reading taken
   - Compressor and valve turned OFF
5. Timer restarts measurement cycle
6. Emergency stop available via command

---

## 📡 Communication

Current Implementation:
- Bluetooth Serial (mobile pairing)

Planned Improvements:
- MQTT over WiFi
- TLS encryption
- Multi-device scalability

---

## 🔬 Engineering Considerations

- Inductive load switching protection
- ESP32 GPIO current limitations
- ADC noise stability and grounding
- Real-time embedded timing using hardware timers
- Medical device data reliability
- System scalability for hospital infrastructure

---

## 🛠 Future Improvements

- Replace pressure sensor with calibrated medical-grade sensor
- Custom PCB for improved EMI control and reliability
- Lithium battery integration
- Secure MQTT implementation
- Improved enclosure ergonomics

---

## 📄 Full Technical Documentation

Full methodology, testing results, and analysis available here:

[Stage 3 Report](report/Stage_3_Report.pdf)

---

## ⚠ Disclaimer

This device is a prototype developed for academic research purposes only.  
It is not certified for clinical or medical use.

---

## 👨‍💻 Author

Duy Ta, Eric Dickson, Kirra Pozzebon, Aidid Yassin  
Electrical Engineering Student  
Embedded Systems | IoT | Hardware Integration
