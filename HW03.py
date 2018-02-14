import pymongo
from datetime import datetime,date
from flask import Flask,request
from flask_restful import Resource ,Api ,reqparse

client = pymongo.MongoClient('localhost',27017)

app= Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('id')
parser.add_argument('username')
parser.add_argument('password')
parser.add_argument('firstname')
parser.add_argument('lastname')
parser.add_argument('employee_number')

db = client.db_example1

class Registration(Resource):
        def post(self):
                args = parser.parse_args()
                id = args['employee_number']
                firstname = args['firstname']
                lastname = args['lastname']
                password = args['password']
                data = work.find_one({"user.employee_number":id})
                if(data):
                        return {"system":"ID is already in the system"}
                work.insert({"user":{"employee_number":id,"firstname":firstname,"lastname":lastname,"password":password},"work_list":[]})
                return {"firstname":firstname,"lastname":lastname,"employee_number":id,"password":password}

class Login(Resource):
        def post(self):
                args = parser.parse_args()
                username = args['username']
                password = args['password']
                data = work.find_one({"user.employee_number":username,"user.pastword":password})
                if(data):
                        firstname = data['user']['firstname']
                        lastname = data['user']['lastname']
                        datetime_login = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                        work.update({"user.employee_number":username},{"$push":{"work_list":{"datetime":datetime_login}}})
                        return {"firstname":firstname,"lastname":lastname,"datetime":datetime_login}
                return {}


work = db.work
class WorkHistory(Resource):
        def get(self):
                args = parser.parse_args()
                id = args['id']
                data = work.find_one({"user.employee_number":id})
                if(data):
                        firstname = data['user']['firstname']
                        lastname = data['user']['lastname']
                        work_list = data['work_list']
                        return {"firstname":firstname,"lastname":lastname,"work_list":work_list}

api.add_resource(Registration,'/api/register')
api.add_resource(Login,'/api/login')
api.add_resource(WorkHistory,'/api/listwork')

if __name__ == '__main__':
        app.run(host='0.0.0.0',port=5005)

# 305445HW3_58364722
