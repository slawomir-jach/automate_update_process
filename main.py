
import json
import requests
import justext
import sys
from request_info import Request


def campare_gradle():

    with open("info_files/current_version.json", "r") as read_file:
        data = json.load(read_file)
        if data["Aps"]["Gradle"]["version"] == Request.gradle_ver():
            print("Gradle is in the same version as in project")
        else:
            print("New Gradle version !!!")


campare_gradle()


def campare_maven():

    with open("info_files/current_version.json", "r") as read_file:
        data = json.load(read_file)
        if data["Aps"]["Maven"]["version"] == Request.maven_ver():
            print("Maven is in the same version as in project")
        else:
            print("New Maven version !!!")


campare_maven()


def campare_ndk():

    with open("info_files/current_version.json", "r") as read_file:
        data = json.load(read_file)
        if data["Aps"]["Android NDK"]["version"] == Request.ndk_ver():
            print("NDK is in the same version as in project")
        else:
            print("New NDK version !!!")


campare_ndk()


def campare_sdk():

    with open("info_files/current_version.json", "r") as read_file:
        data = json.load(read_file)
        if data["Aps"]["Android SDK"]["version"] == Request.sdk_ver():
            print("SDK is in the same version as in project")
        else:
            print("New SDK version !!!")


campare_sdk()


def campare_infer():

    with open("info_files/current_version.json", "r") as read_file:
        data = json.load(read_file)
        if data["Aps"]["Infer"]["version"] == Request.infer_ver():
            print("Infer is in the same version as in project")
        else:
            print("New Infer version !!!")


campare_infer()


def campare_ant():

    with open("info_files/current_version.json", "r") as read_file:
        data = json.load(read_file)
        if data["Aps"]["Ant"]["version"] == Request.ant_ver():
            print("Ant is in the same version as in project")
        else:
            print("New Ant version !!!")


campare_ant()




