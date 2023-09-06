import sys
import os


#change working dir to script dir


#path = '../python_mqtt_interface'
#sys.path.append(path)

curr_dir = os.getcwd()
rel_dir = 'Energy_monitoring\python_mqtt_interface'
#print(curr_dir)
script_dir = os.path.join(curr_dir,rel_dir)
#print(script_dir)
os.chdir(script_dir)


from publish import publishToTopic
import aws_conn_config as acc
import json
import time

""" topic = "machines/machine1"

# Sample JSON data
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

payload = json.dumps(data) """


def wrapperForMatlab(topic, payload):
    """ 
    -- debug lines
    while(True):
        publishToTopic(acc.myMQTTClient, topic, payload)
        print("")
        time.sleep(5) """
    
    try:
        publishToTopic(acc.myMQTTClient, topic, payload)
    except:
        print("Error Occurred, could not publish one datapoint. Moving on...")

    

wrapperForMatlab(topic, payload)


#preserve environment after script returns
os.chdir(curr_dir)