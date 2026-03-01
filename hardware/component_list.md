# Bill of Materials (BOM)
Wireless Blood Pressure Device (ESP32)

Project: Engineering Technology Innovation  
Author: Duy Ta  
Revision: Prototype V1.0  

---

## 1. Electronics Components

| Item No. | Component | Specification / Description | Qty | Function |
|----------|-----------|----------------------------|-----|----------|
| 1 | ESP32 Development Board | 240 MHz dual-core MCU, WiFi & Bluetooth | 1 | Main controller |
| 2 | Pressure Sensor | Analog pressure transducer (cuff measurement) | 1 | Measures cuff pressure |
| 3 | HX711 | 24-bit ADC load cell amplifier | 1 | Signal amplification & ADC |
| 4 | Air Compressor | Mini DC air pump (5V) | 1 | Inflates cuff |
| 5 | Air Valve | DC solenoid valve (3V–5V) | 1 | Controlled deflation |
| 6 | NPN Transistor (or MOSFET) | Used as low-side switch | 2 | Drives pump & valve |
| 7 | Flyback Diode | Fast recovery diode (e.g., 1N4148 / 1N5819) | 2 | Inductive load protection |
| 8 | Base/Gate Resistor | 270Ω (as per schematic) | 2 | Limits control current |
| 9 | Power Supply | 5V regulated supply (Power bank) | 1 | System power source |

---

## 2. Mechanical Components

| Item No. | Component | Description | Qty | Notes |
|----------|-----------|------------|-----|------|
| 10 | Blood Pressure Cuff | Inflatable arm cuff | 1 | Pneumatic interface |
| 11 | Air Tubing | Flexible pneumatic tubing | As required | Connects pump, valve & cuff |
| 12 | 3D Printed Enclosure | Custom housing (PLA prototype) | 1 | Mechanical protection |

---

## 3. Electrical Design Notes

- Compressor and valve are inductive loads.
- Flyback diodes are mandatory to prevent back-EMF damage.
- ESP32 GPIO pins must not directly drive motors or solenoids.
- Proper grounding is required for HX711 stability.
- Separate analog and power ground recommended for PCB revision.
- Decoupling capacitors recommended near ESP32 and HX711.

---

## 4. Future Hardware Revision (Planned)

- Custom PCB with proper ground plane
- Dedicated motor driver or logic-level MOSFET
- Lithium battery charging circuit
- EMI noise filtering for ADC stability
- Medical-grade pressure sensor upgrade
