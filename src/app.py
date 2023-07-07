from flask import Flask
from flask_restful import Api
from controller.controller import Jobs
from controller.controller import TakeJobs
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__)
api = Api(app)

# pymysql.install_as_MySQLdb()

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:lala102030@localhost:3306/teste"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS '] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_RECORD_QUERIES"] = True

app.config['TESTING'] = True

api.add_resource(Jobs, '/jobs/<string:search>/')
api.add_resource(TakeJobs, '/takejobs/<string:search>/<int:page>/<int:limit>')


if __name__ == '__main__':
    from sql_alchemy import db
    # Inicialize o SQLAlchemy com o aplicativo Flask
    db.init_app(app)
    app.run(debug=True, port="3001", host="0.0.0.0")
