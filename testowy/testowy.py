import requests
import json


#with open("gradle_web.json", "r") as ppp:
#
#    data = json.load(ppp)
#
#
#    print(data)

def fabric_ver():
    response = requests.get("https://api.github.com/repos/fabric/fabric/tags")
    todos = json.loads(response.text)
    print(todos[3]["name"])
    return todos[3]["name"]

fabric_ver()

