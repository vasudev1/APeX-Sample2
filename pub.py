#!/usr/bin/python3.5

import sys
import signal
import time
import random
import json
import paho.mqtt.client as mqtt

def on_connect(mqttc, obj, flags, rc):
    print("rc: "+str(rc))

def on_message(mqttc, obj, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

def on_publish(mqttc, obj, mid):
    print("messageID: "+str(mid))
    pass

def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_log(mqttc, obj, level, string):
    print(string)

def randomNum(low, high):
    return random.random() * (high - low) + low

def signal_handler(signal, frame):
    sys.exit(0)

mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe

mqttc.connect("localhost", 1883, 60)

mqttc.loop_start()
signal.signal(signal.SIGINT, signal_handler)
while (True):
    #Accelerometer Data
    accelX = randomNum(0, 1)
    accelY = randomNum(0, 1)
    accelZ = randomNum(0, 1)
    temp = randomNum(0, 110)
    telemetryData = json.dumps({'accelX': accelX, 'accelY': accelY, 'accelZ': accelZ, 'temperature': temp})
    (rc, mid) = mqttc.publish("apex_mqtt", telemetryData, qos=2)

#print("apex_mqtt")
#(rc, mid) = mqttc.publish("apex_mqtt", "bar", qos=2)
#print("class")
#infot = mqttc.publish("class", "bar", qos=2)

#infot.wait_for_publish()
