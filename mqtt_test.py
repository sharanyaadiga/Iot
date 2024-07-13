import paho.mqtt.client as mqtt
import time
# brokerURL = "mqtt.eclipseprojects.io"
brokerURL = "test.mosquitto.org"
brokerPort = 1883 # port number for unencrypted connections

def on_connect(client, userdata, flags, rc):
   print("Connected with result code "+str(rc))

def on_message(client, userdata, message):
   print("Received message '" + str(message.payload) + "' on topic '"
        + message.topic + "' with QoS " + str(message.qos))

def on_disconnect(client, userdata, rc):
    print("Client Got Disconnected")

mqttclient = mqtt.Client() #create cliet object

mqttclient.on_connect = on_connect
mqttclient.on_disconnect = on_disconnect
mqttclient.on_message = on_message

mqttclient.connect(brokerURL, brokerPort) #call connect function with URL and port number

mqttclient.subscribe("HTWIoT/#", qos=1)

mqttclient.loop_start()
# now we can publish topics in the console#

mqttclient.publish(topic="TestingTopic", payload="TestingPayload", qos=0, retain=False)

# to stop use mqttclient.loop_stop()

#Try sending messages: mqttclient.publish("TestingTopic", "Hello")
</code>

