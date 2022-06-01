
import paho.mqtt.publish as publish
import time

# The ThingSpeak Channel ID.
channel_ID = "1754141"

# The hostname of the ThingSpeak MQTT broker.
mqtt_host = "mqtt3.thingspeak.com"

# Your MQTT credentials for the device
mqtt_client_ID = "OSw9PCAEFRkCGwQ1LDEXDgk"
mqtt_username = "OSw9PCAEFRkCGwQ1LDEXDgk"
mqtt_password = "MqI+2z8ei6yHg9spfSqxRH2T"
t_transport = "websockets"
t_port = 80
topic = "channels/" + channel_ID + "/publish"


def increment(counter):

    return counter + 1


def saveDistance(distance):
    publish.single(
        topic,
        payload=distance,
        hostname=mqtt_host,
        transport=t_transport,
        port=t_port,
        client_id=mqtt_client_ID,
        auth={'username': mqtt_username, 'password': mqtt_password}
    )


def main():
    counter = 0

    try:
        while True:
            counter = increment(counter)
            incrementValue = str(counter)
            payload = "field1=" + incrementValue
            print(payload)

            saveDistance(payload)
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("a")


if __name__ == "__main__":
    main()
