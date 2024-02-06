from datetime import datetime
import os
import requests

APP_ID = os.environ.get("APP_ID", "Does not exist")
API_KEY = os.environ.get("API_KEY", "Does not exist")
WEIGHT = 61.2
HEIGHT = 154.94
GSHEET_USER = os.environ.get("GSHEET_USER", "Does not exist")
GSHEET_PASS = os.environ.get("GSHEET_PASS", "Does not exist")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
query = input("How much did you exercise today? ")
exercise_parameters = {
    "query": query,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": "26"
}

response = requests.post(url=exercise_endpoint, json=exercise_parameters, headers=headers)
response.raise_for_status()
data = response.json()

today = datetime.now()
date = today.strftime("%Y%m%d")
time = today.strftime("%r")
workout = data["exercises"][0]["name"]
duration = data["exercises"][0]["duration_min"]
calories = data["exercises"][0]["nf_calories"]

google_sheet_endpoint = "https://api.sheety.co/6ed32ef7a260aaa751babaac33b53a5c/myWorkoutsApiTraining/workouts"

gsheet_headers = {
    "Content-Type": "application/json"
}

gsheet_auth = (GSHEET_USER, GSHEET_PASS)

gsheet_data = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": workout,
        "duration": duration,
        "calories": calories
    }
}

response2 = requests.post(url=google_sheet_endpoint, auth=gsheet_auth, json=gsheet_data, headers=gsheet_headers)
response2.raise_for_status()
print(response2.text)
