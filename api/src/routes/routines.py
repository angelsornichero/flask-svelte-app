from flask import Blueprint, request
from modules.routines_exercises_module import RoutineExercisesModule
from db.database import db
from modules.routines_module import RoutineModule
from modules.jwt_module import JwtModule
from modules.error_module import ErrorResponse

class RoutinesRoutes:

    routines = Blueprint('routines', __name__)

    def __init__(self):
                
        @self.routines.route('/new-routine', methods=['POST'])
        def create_routine():
            name = request.json.get('name')
            label = request.json.get('label')
            token = request.headers.get('authorization')

            verified = JwtModule().verify_jwt(token=token)
            if verified == False:
                return ErrorResponse(401).no_authenticaded_response()

            return RoutineModule(name=name, label=label, token=token).create_routine_module()



        @self.routines.route('/routines', methods=['GET'])
        def get_routines():
            token = request.headers.get('authorization')
            verified = JwtModule().verify_jwt(token=token)
            if verified == False:
                return ErrorResponse(401).no_authenticaded_response()

            return RoutineModule(token=token).get_routines_module()


        @self.routines.route('/routine/<routine_to_delete>', methods=['DELETE'])
        def delete_routine(routine_to_delete):
            token = request.headers.get('authorization')
            verified = JwtModule().verify_jwt(token=token)
            if verified == False:
                return ErrorResponse(401).no_authenticaded_response()
            
            return RoutineModule(token=token).delete_routine_module(routine_to_delete=routine_to_delete)
            


        @self.routines.route('/routine/<routine_to_update>', methods=['PUT'])
        def update_routine(routine_to_update):
            name = request.json.get('name')
            label = request.json.get('label')
            token = request.headers.get('authorization')
            
            verified = JwtModule().verify_jwt(token=token)
            if verified == False:
                return ErrorResponse(401).no_authenticaded_response()
            
            return RoutineModule(token=token, name=name, label=label).update_routine_module(routine_to_update=routine_to_update)

        @self.routines.route('/get-routine/<name>')
        def get_routine(name):
            token = request.headers.get('authorization')
            verified = JwtModule().verify_jwt(token=token)
            if verified == False:
                return ErrorResponse(401).no_authenticaded_response()
            
            return RoutineModule(token=token, name=name).get_routine_module()

        @self.routines.route('/add-exercise', methods=['POST'])
        def add_exercise():
            name = request.json.get('exercise_name')
            routine_name = request.json.get('routine_name')
            reps = request.json.get('reps')
            series = request.json.get('series')
            token = request.headers.get('authorization')
            
            verified = JwtModule().verify_jwt(token=token)
            if verified == False:
                return ErrorResponse(401).no_authenticaded_response()

            return RoutineExercisesModule(token=token, name=name, routine_name=routine_name, reps=reps, series=series).add_exercise()
        
        @self.routines.route('/delete-exercise/<id>', methods=['DELETE'])
        def delete_exercise(id):
            token = request.headers.get('authorization')
            routine_name = request.json.get('routine_name')

            verified = JwtModule().verify_jwt(token=token)
            if verified == False:
                return ErrorResponse(401).no_authenticaded_response()    

            return RoutineExercisesModule(token=token, routine_name=routine_name).delete_exercise(id=id)
        
        