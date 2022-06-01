import requests
import time

headers = {'Content-type': 'application/json'}
url = "https://api.thingspeak.com/update.json"


def sendDistance(distance):

    payload = {
        "api_key": "21ZD22JZNNWJ5FBU",
        "field1": distance,
    }
    res = requests.post(url=url, headers=headers, json=payload)

    print('oi')

    return res.json()


def main():

    try:
        while True:

            time.sleep(0.001)
            print(sendDistance('a'))
    except KeyboardInterrupt:
        print('CYA')


if __name__ == "__main__":
    main()
