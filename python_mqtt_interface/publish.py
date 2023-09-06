from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient


def publishToTopic(MQTTClient_Obj, topic, payload):
    print("Connecting...")
    MQTTClient_Obj.connect()
    print("Client Connected")
    MQTTClient_Obj.publish(topic, payload, 0)  
    print("Message Sent")
    MQTTClient_Obj.disconnect()
    print("Client Disconnected")
