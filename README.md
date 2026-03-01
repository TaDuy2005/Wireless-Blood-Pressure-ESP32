# Wireless Blood Pressure Device (ESP32)

Engineering Technology Innovation Project  
Swinburne University of Technology  
Semester 2, 2024  

## 📌 Overview

This project redesigns an existing commercial blood pressure monitor 
into a wireless IoT-enabled triage device for emergency departments.

The system:
- Inflates cuff using air compressor
- Monitors pressure via pressure sensor
- Automatically deflates at threshold
- Sends readings wirelessly via Bluetooth
- Designed for hospital triage integration

## 🧠 Motivation

Emergency departments experience overcrowding and delays in vital sign monitoring.
This device enables automated and continuous blood pressure monitoring,
reducing triage wait times.

## ⚙️ Hardware Used

- ESP32
- Air compressor (salvaged from Withings device)
- Air valve
- Pressure sensor
- HX711 amplifier
- 3D printed enclosure

## 📡 Communication

- Bluetooth (working prototype)
- MQTT (prototype backend concept)

## 🛠 Features

- Pump ON/OFF control
- Valve ON/OFF control
- Automatic pressure threshold detection
- Periodic measurement via timer interrupt
- Emergency shutoff

## 🧪 Future Improvements

- Replace damaged pressure sensor
- Custom PCB design
- Lithium battery integration
- Secure hospital network integration

## 👨‍💻 Author

Duy Ta, Eric Dickson, Kirra Pozzebon, Aidid Yassin

Electrical Engineering Student
