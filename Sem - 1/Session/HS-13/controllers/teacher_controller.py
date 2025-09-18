from models.teacher import TeacherModel
from flask import Flask,render_template,jsonify,request,Blueprint


teacher = Blueprint('teacher',__name__)

teacher_model = TeacherModel()

@teacher.route('/')
def get_teachers():
    data = teacher_model.get_teachers()
    return jsonify(data),200