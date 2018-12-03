import requests
import pandas as pd
import json


class Request(object):

    @staticmethod
    def ant_ver():
        response = requests.get("https://api.github.com/repos/apache/ant/tags")
        todos = json.loads(response.text)
        return todos[1]["name"]


    @staticmethod
    def gradle_ver():
        response = requests.get("https://services.gradle.org/versions/current")
        todos = json.loads(response.text)
        return todos['version']

    @staticmethod
    def maven_ver():
        response = requests.get("https://api.github.com/repos/apache/maven/tags")
        todos = json.loads(response.text)
        return todos[1]["name"]

    @staticmethod
    def infer_ver():
        response = requests.get("https://api.github.com/repos/facebook/infer/releases/latest")
        todos = json.loads(response.text)
        return todos["tag_name"]

    @staticmethod
    def sdk_ver():
        calls_df = pd.read_html("https://developer.android.com/studio/", header=0, parse_dates=["Platform"])
        var1 = calls_df[1]
        json_file_sdk = var1.to_json()
        data_sdk = json.loads(json_file_sdk)
        return data_sdk["SDK tools package"]["2"]

    @staticmethod
    def ndk_ver():
        calls_ndk = pd.read_html("https://developer.android.com/ndk/downloads/", header=0, parse_dates=["Platform"])
        var1 = calls_ndk[0]
        json_file_ndk = var1.to_json()
        data_ndk = json.loads(json_file_ndk)
        return data_ndk["Package"]["3"]
