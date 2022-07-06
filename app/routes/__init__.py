from .tasks_blueprint import  bp as bp_tasks

from flask import Flask

def init_app(app:Flask):
    app.register_blueprint(bp_tasks)