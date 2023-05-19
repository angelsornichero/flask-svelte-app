from db.database import db
from models.routines import Routines
from modules.jwt_module import JwtModule
from models.routine_exercises import Routines_Exercises

class RoutineModule:


    def __init__(self, token, name=None, label=None):
        self.name = name
        self.label = label
        self.token = token

    def create_routine_module(self):
        if self.name is None or self.label is None:
            return { "message": "[!] Some fields missing", "success": False }, 400
        
        if self.token is None: 
            return { "message": "[!] A token expected", "succes": False }, 401

        self.user = JwtModule().get_user(token=self.token)

        find_routine = Routines.query.filter_by(user=self.user, name=self.name).first()

        if find_routine is not None:
            return { "message": "[!] Routine already exists", "success": False }, 400 

        new_routine = Routines(name=self.name, label=self.label, user=self.user)
        
        db.session.add(new_routine)
        db.session.commit()

        return { 'message': '[*] Routine created successfully', 'success': True } 


    def get_routines_module(self):
        if self.token is None: 
            return { "message": "[!] A token expected", "succes": False }, 401

        self.user = JwtModule().get_user(token=self.token)

        raw_routines = Routines.query.filter_by(user=self.user).all()
        routines = []

        for routine in raw_routines:
            name = routine.name
            label = routine.label
            id = routine.id
            user = routine.user
            timestamps = routine.timestamps

            routines.append({ "name": name, "label": label, "id": id, "user": user, "timestamps": timestamps })


        return { "message": "[*] Here are your routines", "success": True, "routines": routines }

    def delete_routine_module(self, routine_to_delete):
        if self.token is None: 
            return { "message": "[!] A token expected", "succes": False }, 401

        self.user = JwtModule().get_user(token=self.token)

        find_routine = Routines.query.filter_by(name=routine_to_delete, user=self.user).first()

        if find_routine is None:
            return { "message": "[!] Routine doesn't exists", "success": False }

        db.session.delete(find_routine)
        db.session.commit()

        return { "message": "[*] Routine deleted successfully", "success": True }

    def update_routine_module(self, routine_to_update):
        if self.token is None: 
            return { "message": "[!] A token expected", "succes": False }, 401

        self.user = JwtModule().get_user(token=self.token)

        find_routine = Routines.query.filter_by(name=routine_to_update, user=self.user).first()

        if find_routine is None:
            return { "message": "[!] Routine doesn't exists", "success": False }, 400
        
        any_routine = Routines.query.filter_by(name=self.name, user=self.user).first()

        if any_routine is not None:
            return { "message": "[*] There is already a routine with that name", "success": False }, 400
        
        find_routine.name = self.name
        find_routine.label = self.label
        db.session.commit()

        return { "message": "[*] Routine successfully updated", "success": True }
    

    def get_routine_module(self):
        if self.token is None: 
            return { "message": "[!] A token expected", "succes": False }, 401

        self.user = JwtModule().get_user(token=self.token)

        find_routine = Routines.query.filter_by(name=self.name, user=self.user).first()

        if find_routine is None:
            return { "message": "[!] Routine doesn't exists", "success": False }, 400
        
        raw_exercises = Routines_Exercises.query.filter_by(routine_id=find_routine.id).all()
        exercises = []

        for exercise in raw_exercises:
            body_part = exercise.body_part
            id = exercise.id
            equipment = exercise.equipment
            gif_url = exercise.gif_url
            name = exercise.name
            target = exercise.target
            routine_id = exercise.routine_id
            reps = exercise.reps
            series = exercise.series

            exercises.append({ 
                'body_part': body_part, 
                'id': id, 
                'equipment': equipment,
                'gif_url': gif_url,
                'name': name,
                'target': target,
                'routine_id': routine_id,
                'reps': reps,
                'series': series 
            })

        routine = { "name": find_routine.name, "id": find_routine.id, "user": find_routine.user, "label": find_routine.label, "timestapms": find_routine.timestamps }

        return { "message": "[*] Here is your routine", 'routine': routine, 'exercises': exercises, "success": True }
