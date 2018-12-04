
import json
from request_info import Request


def compare_gradle():

    with open("info_files/current_version.json", "r") as read_file:
        data = json.load(read_file)
        if data["Android"]["Gradle"]["version"] == Request.gradle_ver():
            print("Gradle is in the same version as in project")
        else:
            print("New Gradle version !!!")


compare_gradle()


def compare_maven():

    with open("info_files/current_version.json", "r") as read_file:
        data = json.load(read_file)
        if data["Android"]["Maven"]["version"] == Request.maven_ver():
            print("Maven is in the same version as in project")
        else:
            print("New Maven version !!!")


compare_maven()


def compare_ndk():

    with open("info_files/current_version.json", "r") as read_file:
        data = json.load(read_file)
        if data["Android"]["Android NDK"]["version"] == Request.ndk_ver():
            print("NDK is in the same version as in project")
        else:
            print("New NDK version !!!")


compare_ndk()


def compare_sdk():

    with open("info_files/current_version.json", "r") as read_file:
        data = json.load(read_file)
        if data["Android"]["Android SDK"]["version"] == Request.sdk_ver():
            print("SDK is in the same version as in project")
        else:
            print("New SDK version !!!")


compare_sdk()


def compare_infer():

    with open("info_files/current_version.json", "r") as read_file:
        data = json.load(read_file)
        if data["Android"]["Infer"]["version"] == Request.infer_ver():
            print("Infer is in the same version as in project")
        else:
            print("New Infer version !!!")


compare_infer()


def compare_ant():

    with open("info_files/current_version.json", "r") as read_file:
        data = json.load(read_file)
        if data["Android"]["Ant"]["version"] == Request.ant_ver():
            print("Ant is in the same version as in project")
        else:
            print("New Ant version !!!")


compare_ant()


print("############ ios tools version checking #############")


def compare_brew():

    with open("info_files/current_version.json", "r") as read_file:
        data = json.load(read_file)
        if data["Ios"]["Brew"]["version"] == Request.brew_ver():
            print("Brew is in the same version as in project")
        else:
            print("New Brew version !!!")


compare_brew()


def compare_fastline():

    with open("info_files/current_version.json", "r") as read_file:
        data = json.load(read_file)
        if data["Ios"]["Fastlane"]["version"] == Request.fastlane_ver():
            print("Fastlane is in the same version as in project")
        else:
            print("New Fastlane version !!!")


compare_fastline()


def compare_carthage():
    with open("info_files/current_version.json", "r") as read_file:
        data = json.load(read_file)
        if data["Ios"]["Carthage"]["version"] == Request.carthage_ver():
            print("Carthage is in the same version as in project")
        else:
            print("New Carthage version !!!")


compare_carthage()







