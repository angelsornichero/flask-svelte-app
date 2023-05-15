from app import App
from constants.main import PORT

app = App().app

if __name__ == "__main__":
   
   app.run(port=PORT, debug=True)