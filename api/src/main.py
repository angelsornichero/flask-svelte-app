from app import App
from constants.main import PORT, ACTION_ENV
import sys
import time 


app = App().app

if __name__ == "__main__":
   
   app.run(port=PORT, debug=True)
