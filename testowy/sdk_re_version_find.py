import requests
import justext
import re
import readline
#mach = re.search('Released', paragraph.text)

"""This is script for finding new version of SDK Tools , SDK Build tools"""

def sdk_tools_ver():

    response = requests.get("https://developer.android.com/studio/releases/sdk-tools")
    paragraphs = justext.justext(response.content, justext.get_stoplist("English"))
    for paragraph in paragraphs:
        if 'Revision' in paragraph.text:

            #print(paragraph.text)
            p = re.search(r'Revision.*2017', paragraph.text)
            if p:
                print(p)


sdk_tools_ver()


def sdk_buid_tools_ver():


    response = requests.get("https://developer.android.com/studio/releases/build-tools")
    paragraphs = justext.justext(response.content, justext.get_stoplist("English"))
    for paragraph in paragraphs:
        if 'Revision' in paragraph.text:

            # print(paragraph.text)
            p = re.search(r'Revision.*2018', paragraph.text)
            if p:
                print(p)


sdk_buid_tools_ver()
