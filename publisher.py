import paho.mqtt.client as mqtt

mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, 'meu_publisher')

mqtt_client.connect(host="localhost", port=1883)
mqtt_client.publish(topic="/messages", payload="Minha mensagem")