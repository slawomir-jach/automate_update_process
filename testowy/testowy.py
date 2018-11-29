import requests
import json


with open("gradle_web.json", "r") as ppp:

    data = json.load(ppp)

    print(data)
