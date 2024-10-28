from flask import current_app as app, jsonify, render_template,  request, send_file
from flask_security import auth_required, verify_password, hash_password
from backend.models import db
from datetime import datetime
from backend.celery.tasks import add, create_csv
from celery.result import AsyncResult

datastore = app.security.datastore
cache = app.cache

@app.route('/')
def home():
    return render_template('index.html')


@app.get('/celery')
def celery():
    task = add.delay(10, 20)
    return {'task_id' : task.id}

@app.get('/get-csv/<id>')
def getCSV(id):
    result = AsyncResult(id)

    if result.ready():
        return send_file(f'./backend/celery/user-downloads/{result.result}'), 200
    else:
        return {'message' : 'task not ready'}, 405
    
@app.get('/create-csv')
def createCSV():
    task = create_csv.delay()
    return {'task_id' : task.id}, 200

@app.get('/cache')
@cache.cached(timeout = 5)
def cache():
    return {'time' : str(datetime.now())}


@app.get('/protected')
@auth_required('token')
def protected():
    return '<h1> only accessible by auth user</h1>'

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"message" : "invalid inputs"}), 404
    
    user = datastore.find_user(email = email)

    if not user:
        return jsonify({"message" : "invalid email"}), 404
    
    if verify_password(password, user.password):
        return jsonify({'token' : user.get_auth_token(), 'email' : user.email, 'role' : user.roles[0].name, 'id' : user.id})
    
    return jsonify({'message' : 'password wrong'}), 400

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')
    role = data.get('role')

    if not email or not password or role not in ['admin', 'user']:
        return jsonify({"message" : "invalid inputs"}), 404
    
    user = datastore.find_user(email = email)

    if user:
        return jsonify({"message" : "user already exists"}), 404

    try :
        datastore.create_user(email = email, password = hash_password(password), roles = [role], active = True)
        db.session.commit()
        return jsonify({"message" : "user created"}), 200
    except:
        db.session.rollback()
        return jsonify({"message" : "error creating user"}), 400