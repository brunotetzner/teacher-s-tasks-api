from dataclasses import dataclass
from datetime import datetime
from app.configs.database import db  

@dataclass
class TaskModel(db.Model):
    id:          int
    title:        str
    description: str
    finish_date: datetime

    __tablename__ = "tasks"

    id          = db.Column(db.Integer, primary_key=True)
    title       = db.Column(db.String(60), nullable=True)
    description = db.Column(db.String(120))
    finish_date = db.Column(db.String)