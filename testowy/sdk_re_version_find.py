import requests
import justext
import re
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

            #print(paragraph.text)
            p = re.search(r'Revision.*2017', paragraph.text)
            if p:
                print(p)


sdk_tools_ver()


def sdk_build_tools_ver():

    response = requests.get("https://developer.android.com/studio/releases/build-tools")
    paragraphs = justext.justext(response.content, justext.get_stoplist("English"))
    for paragraph in paragraphs:
        if 'Revision' in paragraph.text:

            # print(paragraph.text)
            p = re.search(r'Revision.*2018', paragraph.text)
            if p:
                print(p)


sdk_build_tools_ver()

>>> l = ['element1\t0238.94', 'element2\t2.3904', 'element3\t0139847']
>>> [i.split('\t', 1)[0] for i in l]
['element1', 'element2', 'element3']


