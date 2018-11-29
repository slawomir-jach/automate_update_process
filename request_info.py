import requests
import json


def ant_ver():
    response = requests.get("https://api.github.com/repos/apache/ant/tags")
    todos = json.loads(response.text)

    print(todos[1]["name"])
    return todos[1]["name"]


ant_ver()


def gradle_ver():
    response = requests.get("https://services.gradle.org/versions/current")
    todos = json.loads(response.text)

    print(todos['version'])
    return todos['version']


gradle_ver()


def maven_ver():
    response = requests.get("https://api.github.com/repos/apache/maven/tags")
    todos = json.loads(response.text)

    print(todos[1]["name"])
    return todos[1]["name"]


maven_ver()


def infer_ver():
    response = requests.get("https://api.github.com/repos/facebook/infer/releases/latest")
    todos = json.loads(response.text)

    print(todos["tag_name"])
    return todos["tag_name"]


infer_ver()
