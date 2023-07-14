from flask import Flask
from flask_restful import Api
from controllers.jobs_controller import *
import pymysql
import os





pymysql.install_as_MySQLdb()

app = Flask(__name__, template_folder='view/templates')
api = Api(app)
# socketio = SocketIO(app)

# pymysql.install_as_MySQLdb()
DB_NAME = "teste"
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_PATH = "localhost"

                            
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://root:{DB_PASSWORD}@{DB_PATH}:3306/{DB_NAME}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS '] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_RECORD_QUERIES"] = True

app.config['TESTING'] = True

api.add_resource(Home, '/home')
api.add_resource(Jobs, '/jobs/<string:search>/')
api.add_resource(TakeJobs, '/takejobs/<string:search>/<int:page>/<int:limit>')
api.add_resource(TakeJobsSocket, '/takejobssocket/')



if __name__ == '__main__':
    from sql_alchemy import db
    db.init_app(app)
    app.run(debug=True, port="3001", host="0.0.0.0")
    # app.run(debug=True, port="3001")
