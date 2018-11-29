import requests
import pandas as pd
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


"""This is Pandas librares section """


def sdk_ver():
    calls_df = pd.read_html("https://developer.android.com/studio/", header=0, parse_dates=["Platform"])
    var1 = calls_df[1]
    json_file_sdk = var1.to_json()
    data_sdk = json.loads(json_file_sdk)
    print(data_sdk["SDK tools package"]["2"])


sdk_ver()


def ndk_ver():

    calls_ndk = pd.read_html("https://developer.android.com/ndk/downloads/", header=0, parse_dates=["Platform"])
    var1 = calls_ndk[0]
    json_file_ndk = var1.to_json()
    data_ndk = json.loads(json_file_ndk)
    print(data_ndk["Package"]["3"])


ndk_ver()
