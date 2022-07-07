from flask import jsonify, request
from app.models import TaskModel
from flask import current_app
from sqlalchemy.orm.exc import UnmappedInstanceError
from flask_cors import  cross_origin

@cross_origin()
def create_task_controller():
    data = request.get_json()
    session = current_app.db.session
    new_data = TaskModel(**data)
    session.add(new_data)
    session.commit()

    return jsonify(new_data), 201
   
@cross_origin()
def get_task_controller():
   all_tasks = TaskModel.query.all()
   return jsonify(all_tasks)

@cross_origin()
def patch_task_controller(id):
    try:
        task = TaskModel.query.get(id)
        data = request.get_json()
        session = current_app.db.session

        for key, value in data.items():
             setattr(task, key, value)

        session.add(task)
        session.commit()

        return jsonify(task), 201
    except AttributeError:
        return {"Error": "Task not found"}, 404

@cross_origin()
def delete_task_controller(id):
    try:
        task = TaskModel.query.get(id)
        
        session = current_app.db.session

        session.delete(task)
        session.commit()
        return "", 204

    except UnmappedInstanceError:
        return {"Error": "Task not found"}, 404
