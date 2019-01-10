import requests
import pandas as pd
import json
import justext
import re


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
    def openstf_ver():
        response = requests.get("https://api.github.com/repos/openstf/stf/releases/latest")
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

    @staticmethod
    def brew_ver():
        response = requests.get("https://api.github.com/repos/Homebrew/brew/releases/latest")
        todos = json.loads(response.text)
        return todos["tag_name"]

    @staticmethod
    def fastlane_ver():
        response = requests.get("https://api.github.com/repos/fastlane/fastlane/releases/latest")
        todos = json.loads(response.text)
        return todos["tag_name"]

    @staticmethod
    def carthage_ver():
        response = requests.get("https://api.github.com/repos/fastlane/fastlane/releases/latest")
        todos = json.loads(response.text)
        return todos["tag_name"]

    @staticmethod
    def xcode_ver():
        response = requests.get("https://developer.apple.com/documentation/xcode_release_notes")
        paragraphs = justext.justext(response.content, justext.get_stoplist("English"))
        for paragraph in paragraphs:
            if "ArticleXcode" in paragraph.text:
                ver = paragraph.text.split()[1]
                return ver
            break

    @staticmethod
    def fabric_ver():
        response = requests.get("https://api.github.com/repos/fabric/fabric/tags")
        todos = json.loads(response.text)
        return todos[3]["name"]

    @staticmethod
    def spoon_ver():
        response = requests.get("https://api.github.com/repos/square/spoon/tags")
        todos = json.loads(response.text)
        return todos[0]["name"]

    @staticmethod
    def appledoc_ver():
        response = requests.get("https://api.github.com/repos/tomaz/appledoc/releases/latest")
        todos = json.loads(response.text)
        return todos["tag_name"]

    @staticmethod
    def jazzy_ver():
        response = requests.get("https://api.github.com/repos/realm/jazzy/releases/latest")
        todos = json.loads(response.text)
        return todos["tag_name"]

    @staticmethod
    def swiftlint_ver():
        response = requests.get("https://api.github.com/repos/realm/SwiftLint/releases/latest")
        todos = json.loads(response.text)
        return todos["tag_name"]

    @staticmethod
    def oclint_ver():
        response = requests.get("https://api.github.com/repos/oclint/oclint/releases/latest")
        todos = json.loads(response.text)
        return todos["tag_name"]

    @staticmethod
    def sdk_tools_ver():

        response = requests.get("https://developer.android.com/studio/releases/sdk-tools")
        paragraphs = justext.justext(response.content, justext.get_stoplist("English"))
        for paragraph in paragraphs:
            if 'Revision' in paragraph.text:
                p = re.search('Revision.*\s', paragraph.text)
                if p:
                    a = p.group().split()
                    return a[1]

    @staticmethod
    def sdk_build_tools_ver():

        response = requests.get("https://developer.android.com/studio/releases/build-tools")
        paragraphs = justext.justext(response.content, justext.get_stoplist("English"))
        for paragraph in paragraphs:
            if 'Revision' in paragraph.text:

                # print(paragraph.text)
                p = re.search(r'Revision.*\s', paragraph.text)
                if p:
                    a = p.group().split()
                    return a[1]
