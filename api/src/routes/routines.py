from flask import Blueprint, request
import jwt
from constants.main import JWT_SECRET
from db.database import db
from models.routines import Routines

routines = Blueprint('routines', __name__)

@routines.route('/new-routine', methods=['POST'])
def create_routine():
    name = request.json.get('name')
    label = request.json.get('label')
    token = request.headers.get('authorization')

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



@routines.route('/routines', methods=['GET'])
def get_routines():
    token = request.headers.get('authorization')

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


    return { "message": "[*] Here are your routines", "success": True, "routines": routines}

@routines.route('/routine/<routine_to_delete>', methods=['DELETE'])
def delete_routine(routine_to_delete):
    token = request.headers.get('authorization')
    
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


@routines.route('/routine/<routine_to_update>', methods=['PUT'])
def update_routine(routine_to_update):
    name = request.json.get('name')
    label = request.json.get('label')
    token = request.headers.get('authorization')
    
    if token is None: 
        return { "message": "[!] A token expected", "succes": False }, 401

    decoded = jwt.decode(token, JWT_SECRET, algorithms="HS256")

    username = decoded['username']

    find_routine = Routines.query.filter_by(name=routine_to_update, user=username).first()

    if find_routine is None:
        return { "message": "[!] Routine doesn't exists", "success": False }
    
    find_routine.name = name
    find_routine.label = label

    db.session.commit()

    return { "message": "[*] Routine successfully updated", "success": True }