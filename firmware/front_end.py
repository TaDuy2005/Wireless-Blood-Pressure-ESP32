import tkinter as tk
from tkinter import messagebox
import paho.mqtt.client as mqtt
from random import randrange, uniform
from tkinter import scrolledtext
import time

#initilise constants, global variables
BROKER_NAME = "136.186.230.35"
CLIENT_NAME = "Device 1"
USERNAME = "monitor"
PASSWORD = "reView3"
heartAverage = ""
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
msg = ""
first = True

#on connection
def submit():
    fName = entryF_Name.get()
    lName = entryL_Name.get()
    age = entry_age.get()
    sex = entry_sex.get()

    #verify all fields have attributes
    if(fName == '' or lName == '' or age == '' or sex == ''):
        messagebox.showerror(title="Error",message="Please enter all fields")
        return

    textbox.config(state=tk.NORMAL)
    textbox.insert(tk.END, f"\nFirst name: {fName}\nLast name: {lName}\nAge: {age}\nSex: {sex}\n")
    textbox.config(state=tk.DISABLED)

    #initialise client connection and details
    client = mqtt.Client(CLIENT_NAME)
    client.on_connect = on_connect
    client.username_pw_set(USERNAME, PASSWORD)
    client.tls_set(ca_certs="C:/Users/ericd/OneDrive - Swinburne University/Moar networks/Project/TNE30024_Project_Config_Files/test/server.crt")
    client.tls_insecure_set(False)
    client.connect(BROKER_NAME, port=8883) 
    #subscribe and start MQTT
    client.subscribe("public/#")
    client.on_message = on_message
    client.loop_start() 

#checks if MQTT connection made
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        textbox.config(state=tk.NORMAL)
        textbox.insert(tk.END, f"\n{current_time}: Connected to server\n")
        textbox.config(state=tk.DISABLED)
        client.publish("public", f"'{CLIENT_NAME}' is connected\n",2) 
    else:
        textbox.config(state=tk.NORMAL)
        textbox.insert(tk.END, "Cannot connect, please contact IT\n")
        textbox.config(state=tk.DISABLED)

#checks for incoming MQTT message, data parsing
def on_message(client, userdata, message): 
    textbox.config(state=tk.NORMAL)
    textbox.insert(tk.END, f"{current_time}: {message.payload.decode("utf-8")}\n")
    textbox.config(state=tk.DISABLED)  

    msg = message.payload.decode("utf-8")
    bp_data = msg.split("/")
    if len(bp_data)==2:
        bp_data[0] = int(bp_data[0])
        bp_data[1] = int(bp_data[1])
        #high blood pressure
        if bp_data[0] >=140 and bp_data[1] >= 90:
            messagebox.showerror(title="PATIENT DANGER",message=f"BP HIGH::Patient {entryF_Name.get()} {entryL_Name.get()} with device {CLIENT_NAME} requries urgent medical attention")
        #low blood pressure
        if bp_data[0] <=90 and bp_data[1] <= 60:
            messagebox.showerror(title="PATIENT DANGER",message=f"BP LOW::Patient {entryF_Name.get()} {entryL_Name.get()} with device {CLIENT_NAME} requries urgent medical attention")

#GUI set up
root = tk.Tk()
root.title("GUI Prototype")
frame1 = tk.Frame(root)
frame2 = tk.Frame(root)

frame1.pack(side=tk.LEFT)
frame2.pack(side=tk.RIGHT)

##window layout and attributes##
#left window
submit_button = tk.Button(frame1, text="Device 1",font=("Arial",24))
submit_button.pack(padx=10,pady=10)

submit_button = tk.Button(frame1, text="Device 2",font=("Arial",24))
submit_button.pack(padx=10,pady=10)

#right window
tk.Label(frame2, text="First Name",font=("Arial",24)).pack()
entryF_Name = tk.Entry(frame2,font=("Arial",24))
entryF_Name.pack(padx=10)

tk.Label(frame2, text="Last Name",font=("Arial",24)).pack()
entryL_Name = tk.Entry(frame2,font=("Arial",24))
entryL_Name.pack(padx=10)

tk.Label(frame2, text="Age",font=("Arial",24)).pack()
entry_age = tk.Entry(frame2,font=("Arial",24))
entry_age.pack(padx=10)

tk.Label(frame2, text="Sex",font=("Arial",24)).pack()
entry_sex = tk.Entry(frame2,font=("Arial",24))
entry_sex.pack(padx=10)

submit_button = tk.Button(frame2, text="Submit", font=("Arial",24),command= submit)
submit_button.pack(padx=10,pady=10)

textbox = scrolledtext.ScrolledText(frame2, height=10, width=30,font=("Arial",24))
textbox.insert(tk.END, "User data")
textbox.config(state=tk.DISABLED,font=("Arial",24,))
textbox.pack(padx=10,pady=10)

#start window
root.mainloop()
