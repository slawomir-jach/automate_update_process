import requests
import justext
import re
from request_info import Request
import argparse
import sys
import readline
#mach = re.search('Released', paragraph.text)

"""This is script for finding new version of SDK Tools , SDK Build tools"""


def sdk_tools_ver():

    response = requests.get("https://developer.android.com/studio/releases/sdk-tools")
    paragraphs = justext.justext(response.content, justext.get_stoplist("English"))
    for paragraph in paragraphs:
        if 'Revision' in paragraph.text:
            p = re.search('Revision.*\s', paragraph.text)
            if p:
                a = p.group().split()
                return a[1]



sdk_tools_ver()


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



sdk_build_tools_ver()

print(sdk_build_tools_ver())
print(sdk_tools_ver())

def compare_sdk():

    with open("info_files/current_version.json", "r") as read_file:
        data = json.load(read_file)
        if data["Android"]["Android SDK"]["version"] == Request.sdk_ver():
            print("SDK is in the same version as in project")
        else:
            print("New SDK version !!!")


#compare_sdk()


