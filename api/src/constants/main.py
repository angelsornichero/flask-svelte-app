import os
from dotenv import load_dotenv

load_dotenv()

PORT = os.getenv('PORT')
SQL_URI = os.getenv('SQL_URI')
JWT_SECRET = os.getenv('JWT_SECRET')
X_RAPIDAPI_KEY = os.getenv('X-RapidAPI-Key')
X_RAPIDAPI_HOST = os.getenv('X-RapidAPI-Host')