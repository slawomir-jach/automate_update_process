import requests
import justext

response = requests.get("https://dl.google.com/dl/android/maven2/index.html")
paragraphs = justext.justext(response.content, justext.get_stoplist("English"))
for paragraph in paragraphs:
       print(paragraph.text)
