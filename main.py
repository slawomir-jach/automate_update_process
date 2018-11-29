

import requests
import justext

response = requests.get("")
paragraphs = justext.justext(response.content, justext.get_stoplist("English"))
for paragraph in paragraphs:
    print(paragraph.text)
