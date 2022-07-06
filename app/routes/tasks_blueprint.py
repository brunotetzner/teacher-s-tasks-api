from flask import Blueprint

from app.controllers import *
from app.controllers.tasks_controller import delete_task_controller, get_task_controller, patch_task_controller 

bp = Blueprint("bp_categories", __name__, url_prefix="/api/tasks")

bp.get("")(get_task_controller)
bp.post("")(create_task_controller)
bp.patch("/<int:id>")(patch_task_controller)
bp.delete("/<int:id>")(delete_task_controller)
