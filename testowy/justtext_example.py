import requests
import justext
import sys


def xcode_ver():
    response = requests.get("https://developer.apple.com/documentation/xcode_release_notes")
    paragraphs = justext.justext(response.content, justext.get_stoplist("English"))
    for paragraph in paragraphs:
        if "ArticleXcode" in paragraph.text:
            ver = paragraph.text.split()[1]
            return ver
        break



        #print(release_list)

