import os
from dotenv import load_dotenv

load_dotenv()

PORT = os.getenv('PORT')
SQL_URI = os.getenv('SQL_URI')