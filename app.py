#!/bin/env python3.5

import os
import logging
import json
import sys
from flask import Flask, render_template, jsonify
from flask.ext.bower import Bower
from flask.ext.bcrypt import Bcrypt
import config
from model.shared import db, ma
from model.data_models import University, Company
from model.data_schema import *

app = Flask(__name__)
Bower(app)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.DEBUG)
app.config.from_pyfile('config.py')

db.init_app(app)
ma.init_app(app)

@app.route('/')
def Index():
  return render_template('index.html')

# for debugging
@app.route('/services')
def Services():
  return jsonify(config.SERVICES)

@app.route('/login', methods=['POST'])
def login():
  data = request.json
  return 'Student %s' % username

@app.route('/dashboard')
def dashboard():
  return 'Dashboard'


## Single Entries
@app.route('/university/<id>')
def show_university(id):
  university = University.query.filter_by(id=id).first()
  return jsonify({'university': university_schema.dump(university).data})

@app.route('/professor/<id>')
def show_professor(id):
  professor = Professor.query.filter_by(id=id).first()
  return jsonify({'professor': professor_schema.dump(professor).data})

@app.route('/course/<id>')
def show_course(id):
  course = Course.query.filter_by(id=id).first()
  return jsonify({'course': course_schema.dump(course).data})

@app.route('/project/<id>')
def show_project(id):
  project = Project.query.filter_by(id=id).first()
  return jsonify({'project': project_schema.dump(project).data})

@app.route('/company/<id>')
def show_company(id):
  company = Company.query.filter_by(id=id).first()
  return jsonify({'company': company_schema.dump(company).data})

@app.route('/skill/<id>')
def show_skill(id):
  skill = Skill.query.filter_by(id=id).first()
  return jsonify({'skill': skill_schema.dump(skill).data})

@app.route('/student/<id>')
def show_student(id):
  student = Student.query.filter_by(id=id).first()
  return jsonify({'student': student_schema.dump(student).data})

@app.route('/account/<id>')
def show_account(id):
  account = Account.query.filter_by(id=id).first()
  return jsonify({'account': account_schema.dump(account).data})

## List Entries
@app.route('/university')
def show_universities():
  universities = University.query.all()
  return jsonify({'universities': universities_schema.dump(universities).data})

@app.route('/professor')
def show_professors():
  professors = Professor.query.all()
  return jsonify({'professors': professors_schema.dump(professors).data})

@app.route('/course')
def show_courses():
  courses = Course.query.all()
  return jsonify({'courses': courses_schema.dump(courses).data})

@app.route('/project')
def show_projects():
  projects = Project.query.all()
  return jsonify({'projects': projects_schema.dump(projects).data})

@app.route('/company')
def show_companies():
  companies = Company.query.all()
  return jsonify({'companies': companies_schema.dump(companies).data})

@app.route('/skill')
def show_skills():
  skills = Skill.query.all()
  return jsonify({'skills': skills_schema.dump(skills).data})

@app.route('/student')
def show_students():
  students = Student.query.all()
  return jsonify({'students': students_schema.dump(students).data})

@app.route('/account')
def show_accounts():
  accounts = Account.query.all()
  return jsonify({'accounts': accounts_schema.dump(accounts).data})


port = os.getenv('VCAP_APP_PORT', '5000')
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=int(port))