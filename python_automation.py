import requests
import schedule
import time


def send_message():
    resp = requests.post('https://textbelt.com/text', {
        "phone": +254713219373,
        "message": "Hey, goodmorning",
        "key": "textbelt"

    })
    print(resp.json())


# schedule.every().day.at("06":00).do(send_message)
schedule.every(10).seconds.do(send_message())

while True:
    schedule.run_pending()
    time.sleep(1)

# this program works the error message displayed therein is proof wnough
