import requests
import json
from datetime import datetime

def getstatus():
    response = requests.get("https://www.githubstatus.com/api/v2/summary.json")
    text = json.loads(response.text)
    components = text["components"]

    name = ""
    status = ""

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Time: "+current_time)

    for component in components:
        for key, value in component.items():
            if key == "name":
                if value == "Visit www.githubstatus.com for more information":
                    break
                name = value
            if key == "status":
                status = value
            if name != "" and status != "":
                print("The current status of %s is %s" % (name, status))
                name = ""
                status = ""


while True:
    copyyn = str(input('Would you like the current status of GitHub? (Y/N)'))
    if copyyn == "Y":
        getstatus()
    else:
        break
