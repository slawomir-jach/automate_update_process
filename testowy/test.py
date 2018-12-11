import requests
import pandas as pd
import json
import justext
import re




def spoon_ver():
    response = requests.get("https://api.github.com/repos/square/spoon/tags")
    todos = json.loads(response.text)
    print(todos[0]["name"])
    return todos[0]["name"]

spoon_ver()



