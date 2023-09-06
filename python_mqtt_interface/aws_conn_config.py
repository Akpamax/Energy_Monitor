from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

#Configure connection parameters 
endpoint                = "a1gv9csz01r9tt-ats.iot.eu-west-1.amazonaws.com"
port                    = 8883
device_cert_path        = "./certs/certificate.crt"
private_key_cert_path   = "./certs/private_key.key"
root_auth_cert_path     = "./certs/root_cert.pem"

# For certificate based connection
myMQTTClient = AWSIoTMQTTClient("client1")

# For TLS mutual authentication
myMQTTClient.configureEndpoint(endpoint, 8883) 
myMQTTClient.configureCredentials(root_auth_cert_path, private_key_cert_path, device_cert_path) 
myMQTTClient.configureOfflinePublishQueueing(-1)
myMQTTClient.configureDrainingFrequency(2)
myMQTTClient.configureConnectDisconnectTimeout(10)
myMQTTClient.configureMQTTOperationTimeout(5)


#topic = "machines/machine1"
