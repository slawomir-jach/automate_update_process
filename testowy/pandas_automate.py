import pandas as pd
import json


def sdk_ver():
    calls_df = pd.read_html("https://developer.android.com/studio/", header=0, parse_dates=["Platform"])
    var1 = calls_df[1]
    json_file_sdk = var1.to_json()
    data_sdk = json.loads(json_file_sdk)
    print(data_sdk["SDK tools package"]["2"])


sdk_ver()



calls_ndk = pd.read_html("https://developer.android.com/ndk/downloads/" , header=0, parse_dates=["Platform"])
var2 = calls_ndk[0]


json_file_sdk = var1.to_json()
json_file_ndk = var2.to_json()

data_sdk = json.loads(json_file_sdk)
print(data_sdk["SDK tools package"]["2"])
data_ndk = json.loads(json_file_ndk)
print(data_ndk["Package"]["3"])


#print(json_file_sdk[4])
#print(json_file_ndk)


#ant = pd.read_html("https://ant.apache.org/antnews.html")
#print(ant)

#tables = pd.read_html("https://developer.android.com/studio/")

#print(tables[1])
