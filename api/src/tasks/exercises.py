import requests
from constants.main import X_RAPIDAPI_HOST, X_RAPIDAPI_KEY 
from models.exercises import Exercises

def get_exercises():

    find_exercises = Exercises.query.all()

    if len(find_exercises) != 0:
        print('[*] Database is already complete, exiting')
    

    print('[*]: Collecting exercises')
    

    url = "https://exercisedb.p.rapidapi.com/exercises"

    headers = {
        "X-RapidAPI-Key": X_RAPIDAPI_KEY,
        "X-RapidAPI-Host": X_RAPIDAPI_HOST
    }

    response = requests.get(url, headers=headers)

    print(response.json())
