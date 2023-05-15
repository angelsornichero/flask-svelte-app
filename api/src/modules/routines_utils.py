import jwt
from constants.main import JWT_SECRET
from db.database import db
from models.routines import Routines
from flask import request

def create_routine_module(name, label, token):
    if name is None or label is None:
        return { "message": "[!] Some fields missing", "success": False }, 400
    
    if token is None: 
        return { "message": "[!] A token expected", "succes": False }, 401

    decoded = jwt.decode(token, JWT_SECRET, algorithms="HS256")

    username = decoded['username']

    find_routine = Routines.query.filter_by(user=username, name=name).first()

    if find_routine is not None:
        return { "message": "[!] Routine already exists", "success": False }, 400 

    new_routine = Routines(name=name, label=label, user=username)
    
    db.session.add(new_routine)
    db.session.commit()

    return { 'message': '[*] Routine created successfully', 'success': True } 


def get_routines_module(token):
    if token is None: 
        return { "message": "[!] A token expected", "succes": False }, 401

    decoded = jwt.decode(token, JWT_SECRET, algorithms="HS256")

    username = decoded['username']

    raw_routines = Routines.query.filter_by(user=username).all()
    routines = []

    for routine in raw_routines:
        name = routine.name
        label = routine.label
        id = routine.id
        user = routine.user
        timestamps = routine.timestamps

        routines.append({ "name": name, "label": label, "id": id, "user": user, "timestamps": timestamps })


    return { "message": "[*] Here are your routines", "success": True, "routines": routines }

def delete_routine_module(token, routine_to_delete):
    if token is None: 
        return { "message": "[!] A token expected", "succes": False }, 401

    decoded = jwt.decode(token, JWT_SECRET, algorithms="HS256")

    username = decoded['username']

    find_routine = Routines.query.filter_by(name=routine_to_delete, user=username).first()

    if find_routine is None:
        return { "message": "[!] Routine doesn't exists", "success": False }

    db.session.delete(find_routine)
    db.session.commit()

    return { "message": "[*] Routine deleted successfully", "success": True }

def update_routine_module(token, routine_to_update, name, label):
    if token is None: 
        return { "message": "[!] A token expected", "succes": False }, 401

    decoded = jwt.decode(token, JWT_SECRET, algorithms="HS256")

    username = decoded['username']

    find_routine = Routines.query.filter_by(name=routine_to_update, user=username).first()

    if find_routine is None:
        return { "message": "[!] Routine doesn't exists", "success": False }, 400
    
    

    any_routine = Routines.query.filter_by(name=name, user=username).first()

    if any_routine is not None:
        return { "message": "[*] There is already a routine with that name", "success": False }, 400
    
    find_routine.name = name
    find_routine.label = label
    db.session.commit()

    return { "message": "[*] Routine successfully updated", "success": True }