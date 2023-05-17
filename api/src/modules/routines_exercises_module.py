from db.database import db
from models.routine_exercises import Routines_Exercises
from models.routines import Routines
from models.exercises import Exercises
from modules.jwt_module import JwtModule


class RoutineExercises:
    
    def __init__(self, token, name, routine_name, reps = None, series = None):
        self.token = token
        self.name = name
        self.routine_name = routine_name
        self.reps = reps
        self.series = series


    def add_exercise(self):

        if self.name is None or self.routine_name is None or self.reps is None or self.series is None:
            return { "message": "There are some fields missing", "success": False }


        if self.token is None: 
            return { "message": "[!] A token expected", "succes": False }, 401

        self.user = JwtModule().get_user(token=self.token)

        find_routine = Routines.query.filter_by(user=self.user, name=self.routine_name).first()

        if find_routine is None:
            return { "message": "[!] Routine doesn't exists", "success": False }, 404 
        
        find_exercise = Exercises.query.filter_by(name=self.name).first()

        if find_exercise is None:
            return { "message": "[!] Exercise doesn't exists", "success": False }, 404 
        
        new_exercise_to_routine = Routines_Exercises(
            name=self.name, 
            body_part=find_exercise.body_part,
            equipment=find_exercise.equipment,
            gif_url=find_exercise.gif_url,
            target=find_exercise.target,
            reps=self.reps,
            series=self.series,
            routine_id=find_routine.id
        )

        db.session.add(new_exercise_to_routine)
        db.session.commit()

        return { "message": "[*] Exercise successfully upload to {}".format(self.routine_name), "success": True }