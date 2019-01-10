#! /usr/bin/env python
import sys, os, json, subprocess, requests, ast
import getopt


#Version 1.0b1
#Author: A187839
#Date: 11-10-2017

def main(argv):

    SERVER_URL= 'http://10.24.73.105'
    ADB_PATH= '/usr/local/android-sdk-linux/platform-tools/adb'

    STF_API_TOKEN = ''
    ANDROID_VERSION = ''
    CMD = ''

    if ((len(sys.argv) != 6)):
        print ("OpenSTF script argument list is not enough, please have look at usage")
        print ("Usage: android-stf-test.py --token <token>  --version <android_version> connect/disconnect")
        sys.exit(1)

    try:
        opts, args = getopt.getopt(argv, "token:version:connect:disconnect", ["token=",  "version=", "connect", "disconnect"])

    except getopt.GetoptError:

        print ("Usage: android-stf-test.py --token <token> --version <android_version> connect/disconnect")
        sys.exit(1)

    for opt, arg in opts:
        if opt == '-h':
            print ("help: android-stf-test.py --token <token>  --version <android_version> --connect <true/false>")
            sys.exit(0)

        elif opt in ("-token", "--token"):
            STF_API_TOKEN = arg
        elif opt in ("-version", "--version"):
            ANDROID_VERSION = arg
        elif opt in ("-connect", "--connect"):
            CMD = arg

    CMD = sys.argv[5]
    
    print ("-> Triggered command line arguments STF_API_TOKEN: "+STF_API_TOKEN+" - ANDROID_VERSION: "+ANDROID_VERSION+" - CMD: "+CMD+"\n")




# connect

 if (str(CMD) == "connect"):

        url = SERVER_URL+"/api/v1/devices"
        token = str(STF_API_TOKEN)
        proxies = {'http': '10.26.238.32:3128'}
        headers = {'Content-type': 'application/json', 'Authorization': "Bearer " + token}

        print ("-> Searching for corresponding OpenSTF devices with version "+ ANDROID_VERSION + "...")

        try:
            response = requests.get(url, proxies=proxies, headers=headers)
            returned_data = json.loads(response.text)

        except requests.exceptions.ConnectTimeout:
            print('ERROR: Connection timeout occured. Please retry later')
            print('-> Details : {content}'.format(content=err.response.content))
            exit(1)
        except requests.exceptions.HTTPError as err:
            print('ERROR: Server error occured. Please retry later')
            print('-> Details : {content}'.format(content=err.response.content))
            exit(1)


        STF_DEVICE_SERIAL = ''

        for row in returned_data['devices']:
            try:
                if (row['using'] == False) and (row['present'] == True):
                    version = row['version'];
                    if version == str(ANDROID_VERSION):
                        STF_DEVICE_SERIAL = row['serial']
                        break;
            except KeyError:
                print("   WARNING: One device doesn't reference a 'version', skipping...")

#no available devices found

 if (str(STF_DEVICE_SERIAL) == str()):
            print("ERROR: Did not find any currently free device matching with the android version "+ ANDROID_VERSION)
            exit(0)
        else:
            print("   SUCCESS: Founded a device corresponding to the android version "+ANDROID_VERSION+" with serial "+ STF_DEVICE_SERIAL+"\n")


        print ("-> Booking the device with serial: "+STF_DEVICE_SERIAL)

        url = SERVER_URL+"/api/v1/user/devices"
        token = str(STF_API_TOKEN)
        serial = str(STF_DEVICE_SERIAL)
        proxies = {'http': '10.26.238.32:3128'}
        headers = {'Content-type': 'application/json', 'Authorization': "Bearer " + token}
        serialNo = {"serial": serial}
        data = json.dumps(serialNo)

        try:
            response = requests.post(url, data=data, proxies=proxies, headers=headers)
            if response.status_code != 200:
                print("ERROR : code: "+ str(response.status_code))
                content = json.loads(response.text)
                print("-> Description: "+content['description'])
                exit(1)
        except requests.exceptions.ConnectTimeout:
            print('ERROR: Connection timeout occured. Please retry later')
            print('--> Details : {content}'.format(content=err.response.content))
            exit(1)
        except requests.exceptions.HTTPError as err:
            print('ERROR: Server error occured. Please retry later')
            print('--> Details : {content}'.format(content=err.response.content))
            exit(1)


        answer = json.loads(response.text)


# answer success / false

 if (answer['success'] == False):
            print("ERROR: OpenSTF service error.")
            remote = json.loads(str(answer.val))
            DESCR = remote['description']
            print ("-> Details: "+ DESCR)
            exit(1)

        else:
            print ("   SUCCESS: Device with serial "+ STF_DEVICE_SERIAL  +" is reserved"+"\n")

            print ("-> Retrieving device details...")
            serial = str(STF_DEVICE_SERIAL)
            url = SERVER_URL+"/api/v1/user/devices/" + serial
            token = str(STF_API_TOKEN)
            proxies = {'http': '10.26.238.32:3128'}
            headers = {'Content-type': 'application/json', 'Authorization': "Bearer " + token}

        try:
            response = requests.get(url, proxies=proxies, headers=headers)
            if response.status_code != 200:
                print("ERROR : code: "+response.status_code)
                content = json.loads(response.text)
                print("-> Description: "+content['description'])
                exit(1)
        except requests.exceptions.ConnectTimeout:
            print('ERROR: Connection timeout occured. Please retry later')
            print('-> Details : {content}'.format(content=err.response.content))
            exit(1)
        except requests.exceptions.HTTPError as err:
            print('ERROR: Server error occured. Please retry later')
            print('-> Details : {content}'.format(content=err.response.content))
            exit(1)

# if status = 200


 if response.status_code == 200:

            INFO = json.loads(response.text)
            MANUFACTURER = INFO['device']['manufacturer']
            MODEL = INFO['device']['model']
            VERSION = INFO['device']['version']
            ABI = INFO['device']['abi']
            REMOTE_URL = INFO['device']['remoteConnectUrl']

            print("   SUCCESS: details of the device, MANUFACTURER:"+str(MANUFACTURER)+" - MODEL:"+str(MODEL)+" - VERSION:"+str(VERSION)+" - ABI:"+str(ABI)+"\n")

            print("-> Searching for the ADB connection for the device...")

            serial = str(STF_DEVICE_SERIAL)
            url = SERVER_URL+"/api/v1/user/devices/" + serial + "/remoteConnect"
            token = str(STF_API_TOKEN)
            proxies = {'http': '10.26.238.32:3128'}
            headers = {'Content-type': 'application/json', 'Authorization': "Bearer " + token}
            serialNo = {"serial": serial}
            data = json.dumps(serialNo)

        try:
            response = requests.post(url, data=data, proxies=proxies, headers=headers)
            if response.status_code != 200:
                print("ERROR : code: "+response.status_code)
                content = json.loads(response.text)
                print("-> Description: "+content['description'])
                exit(1)
        except requests.exceptions.ConnectTimeout:
            print('ERROR: Connection timeout occured. Please retry later')
            print('-> Details : {content}'.format(content=err.response.content))
            exit(1)
        except requests.exceptions.HTTPError as err:
            print('ERROR: Server error occured. Please retry later')
            print('-> Details : {content}'.format(content=err.response.content))
            exit(1)

        RESPONSE = json.loads(response.text)
        STATUS = RESPONSE['success']

        STF_ADB_ADRESS = ''

# additionall lot of code's   to this point




if __name__ == "__main__":
    main(sys.argv[1:])

