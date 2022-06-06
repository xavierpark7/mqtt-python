
import ssl
from paho import mqtt
import paho.mqtt.client as paho
import paho.mqtt.publish as publish

username = ""
password = ""
host = ""
topic = ""
port = ""

# create a messages 
msgs = [{'topic': topic, 'payload': "HURRAY.."}]

sslSettings = ssl.SSLContext(mqtt.client.ssl.PROTOCOL_TLS)

# put in your credentials and hostname
auth = {'username': username, 'password': password}
publish.multiple(msgs, hostname=host, port=port, auth=auth,
                 tls=sslSettings, protocol=paho.MQTTv31)