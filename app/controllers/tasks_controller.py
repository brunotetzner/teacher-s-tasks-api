import json
from flask import jsonify, request
from app.models import TaskModel
from flask import current_app

def create_task_controller():
    data = request.get_json()
    session = current_app.db.session
    new_data = TaskModel(**data)
    session.add(new_data)
    session.commit()

    return jsonify(new_data), 201
   

def get_task_controller():
   all_tasks = TaskModel.query.all()
   return jsonify(all_tasks)

def patch_task_controller():
    return "patching", 200

def delete_task_controller():
    return "deleting", 204