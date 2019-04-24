
import json
from request_info import Request
from os.path import join
import inspect
import types
import sys


def compare_gradle():

    with open("info_files/current_version.json", "r") as read_file:
        data = json.load(read_file)
        if data["Android"]["Gradle"]["version"] == Request.gradle_ver():
            print("Gradle is in the same", (Request.gradle_ver()), "version as in project")
        else:
            print("New Gradle version", (Request.gradle_ver()), "!!!")


compare_gradle()


def compare_maven():

    with open("info_files/current_version.json", "r") as read_file:
        data = json.load(read_file)
        if data["Android"]["Maven"]["version"] == Request.maven_ver():
            print("Maven is in the same", (Request.maven_ver()), "version as in project")
        else:
            print("New Maven version", (Request.maven_ver()), "!!!")


compare_maven()


def compare_ndk():

    with open("info_files/current_version.json", "r") as read_file:
        data = json.load(read_file)
        if data["Android"]["Android NDK"]["version"] == Request.ndk_ver():
            print("NDK is in the same", (Request.ndk_ver()), "version as in project")
        else:
            print("New NDK version", (Request.ndk_ver()), "!!!")


compare_ndk()


def compare_sdktools():
    with open("info_files/current_version.json", "r") as read_file:
        data = json.load(read_file)
        if data["Android"]["Sdktools"]["version"] == Request.sdk_tools_ver():
            print("SDK tools is in the same", (Request.sdk_tools_ver()), "version as in project")
        else:
            print("New SDK Tools version", (Request.sdk_tools_ver()), "!!!")


compare_sdktools()


def compare_sdkbuildtools():
    with open("info_files/current_version.json", "r") as read_file:
        data = json.load(read_file)
        if data["Android"]["Sdkbuildtools"]["version"] == Request.sdk_build_tools_ver():
            print("SDK build tools is in the same", (Request.sdk_build_tools_ver()), "version as in project")
        else:
            print("New SDK build Tools", (Request.sdk_build_tools_ver()), "version !!!")


compare_sdkbuildtools()


def compare_infer():

    with open("info_files/current_version.json", "r") as read_file:
        data = json.load(read_file)
        if data["Android"]["Infer"]["version"] == Request.infer_ver():
            print("Infer is in the same", (Request.infer_ver()), "version as in project")
        else:
            print("New Infer version", (Request.infer_ver()), "!!!")


compare_infer()


def compare_spoon():

    with open("info_files/current_version.json", "r") as read_file:
        data = json.load(read_file)
        if data["Android"]["Spoon"]["version"] == Request.spoon_ver():
            print("Spoon is in the same", (Request.spoon_ver()), "version as in project")
        else:
            print("New Spoon version", (Request.spoon_ver()), "!!!")


compare_spoon()


def compare_openstf():

    with open("info_files/current_version.json", "r") as read_file:
        data = json.load(read_file)
        if data["Android"]["Openstf"]["version"] == Request.openstf_ver():
            print("OpenSTF is in the same version ", (Request.openstf_ver()), "as in project")
        else:
            print("New OpenSTF version !!!")


compare_openstf()


def compare_ant():

    with open("info_files/current_version.json", "r") as read_file:
        data = json.load(read_file)
        if data["Android"]["Ant"]["version"] == Request.ant_ver():
            print("Ant is in the same", (Request.ant_ver()),  "version as in project")
        else:
            print("New Ant version", (Request.ant_ver()),  "!!!")


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


def compare_xcode():
    with open("info_files/current_version.json", "r") as read_file:
        data = json.load(read_file)
        if data["Ios"]["Xcode"]["version"] == Request.xcode_ver():
            print("Xcode is in the same version as in project")
        else:
            print("New Xcode version !!!")


compare_xcode()


def compare_fabric():
    with open("info_files/current_version.json", "r") as read_file:
        data = json.load(read_file)
        if data["Ios"]["Fabric"]["version"] == Request.fabric_ver():
            print("Fabric is in the same version as in project")
        else:
            print("New Fabric version !!!")


def compare_appledoc():
    with open("info_files/current_version.json", "r") as read_file:
        data = json.load(read_file)
        if data["Ios"]["Appledoc"]["version"] == Request.appledoc_ver():
            print("Appledoc is in the same version as in project")
        else:
            print("New Appledoc version !!!")


compare_appledoc()


def compare_jazzy():
    with open("info_files/current_version.json", "r") as read_file:
        data = json.load(read_file)
        if data["Ios"]["Appledoc"]["version"] == Request.jazzy_ver():
            print("Jazzy is in the same version as in project")
        else:
            print("New Jazzy version !!!")


compare_jazzy()


def compare_swiftlint():
    with open("info_files/current_version.json", "r") as read_file:
        data = json.load(read_file)
        if data["Ios"]["Swiftlint"]["version"] == Request.swiftlint_ver():
            print("Swiftlint is in the same version as in project")
        else:
            print("New Swiftlint version !!!")


compare_swiftlint()


def compare_oclint():
    with open("info_files/current_version.json", "r") as read_file:
        data = json.load(read_file)
        if data["Ios"]["Oclint"]["version"] == Request.oclint_ver():
            print("Oclint is in the same version as in project")
        else:
            print("New Oclint version !!!")


compare_oclint()


def compare_sdktools():
    with open("info_files/current_version.json", "r") as read_file:
        data = json.load(read_file)
        if data["Ios"]["Android"]["version"] == Request.oclint_ver():
            print("SDK tools is in the same version as in project")
        else:
            print("New SDK Tools version !!!")


compare_oclint()

def is_local(objectt):
    return isinstance(objectt, types.FunctionType) and objectt.__module__ == __name__


function_list = [name for name, value in inspect.getmembers(sys.modules[__name__], predicate=is_local)]


def version_fun():
    for single_func in function_list:
        print(single_func)


#version_fun()











