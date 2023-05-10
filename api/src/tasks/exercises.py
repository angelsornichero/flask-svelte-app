import requests
from constants.main import X_RAPIDAPI_HOST, X_RAPIDAPI_KEY 
from models.exercises import Exercises
from db.database import db


def get_exercises():

    find_exercises = Exercises.query.all()

    if len(find_exercises) != 0:
        print('[*] Database is already complete, exiting')
        return 
       
    print('[*]: Collecting exercises')
    

    url = "https://exercisedb.p.rapidapi.com/exercises"

    headers = {
        "X-RapidAPI-Key": X_RAPIDAPI_KEY,
        "X-RapidAPI-Host": X_RAPIDAPI_HOST
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    entries = []

    for entry in data:
        new_entry = Exercises(
            body_part=entry['bodyPart'],
            id=entry['id'],
            equipment=entry['equipment'],
            gif_url=entry['gifUrl'],
            name=entry['name'],
            target=entry['target']
        )

        entries.append(new_entry)

    db.session.add_all(entries)
    db.session.commit()

    print('[*] Database filled successfully')