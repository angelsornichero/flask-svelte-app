from app import App
from constants.main import PORT, ACTION_ENV
import sys
import time 


app = App().app

if __name__ == "__main__":
   
   app.run(port=PORT, debug=True)
   if ACTION_ENV == 1:
      time.sleep(3)
      sys.exit(0)
