import json
import requests


def gradle_ver():
    response = requests.get("https://services.gradle.org/versions/current")
    todos = json.loads(response.text)

    print(todos['version'])


gradle_ver()
