from flask import Flask
from views import views


#initialises the application
app = Flask(__name__)

#registers blueprint
app.register_blueprint(views , url_prefix="/")



#starts the server on port 8000
if __name__ == '__main__':
    app.run(debug=True,port=5000)
    