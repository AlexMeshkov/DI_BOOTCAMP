import requests
import json


def get_data():
    lst_iss = []
    try:
        iss = requests.get("HTTP://API.OPEN-NOTIFY.ORG/ISS-NOW.JSON")
        if iss.status_code != 200:
            raise Exception("no data found")
        else:
            python_dict = iss.json()
            lst_iss.append(python_dict)
            # print(f"latitude {python_dict[ 'iss_position']['latitude']}")
        dict_iss[day] = 

        with open("iss.json", "w") as file:
            json.dump(lst_iss, file, indent=4)
    except Exception as err:
        print(err)


get_data()
