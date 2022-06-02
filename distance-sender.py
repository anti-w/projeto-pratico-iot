
import paho.mqtt.client as mqttClient
import time

# The ThingSpeak Channel ID.
channel_ID = "1754141"

# The hostname of the ThingSpeak MQTT broker.
mqtt_host = "mqtt3.thingspeak.com"

# Your MQTT credentials for the device
mqtt_client_ID = "OSw9PCAEFRkCGwQ1LDEXDgk"
mqtt_username = "OSw9PCAEFRkCGwQ1LDEXDgk"
mqtt_password = "MqI+2z8ei6yHg9spfSqxRH2T"
t_port = 1883
topic = "channels/" + channel_ID + "/publish/fields/field1"


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code: %d\n", rc)
    client = mqttClient.Client(mqtt_client_ID)
    client.username_pw_set(mqtt_username, mqtt_password)

    client.on_connect = on_connect
    client.connect(mqtt_host, port=t_port)

    return client


def publish(client, distance):
    result = client.publish(topic, distance)
    status = result[0]

    if status == 0:
        print(f"Send `{distance}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic `{topic}`")


def main():

    count = 0
    client = connect_mqtt()
    client.loop_start()

    try:
        while True:
            countString = str(count)

            publish(client, countString)
            count += 1
            time.sleep(1)

    except KeyboardInterrupt:
        print("a")


if __name__ == "__main__":
    main()
