from shared import db

student_skill = db.Table(
    'student_skill', db.Model.metadata,
    db.Column('rating', db.Integer, nullable=False),
    db.Column('student_id', db.Integer, db.ForeignKey('student.id'), nullable=False),
    db.Column('skill_id', db.Integer, db.ForeignKey('skill.id'), nullable=False)
)

course_skill = db.Table(
    'course_skill', db.Model.metadata,
    db.Column('course_id', db.Integer, db.ForeignKey('course.id'), nullable=False),
    db.Column('skill_id', db.Integer, db.ForeignKey('skill.id'), nullable=False)
)

company_skill = db.Table(
    'company_skill', db.Model.metadata,
    db.Column('company_id', db.Integer, db.ForeignKey('company.id'), nullable=False),
    db.Column('skill_id', db.Integer, db.ForeignKey('skill.id'), nullable=False)
)

project_skill = db.Table(
    'project_skill', db.Model.metadata,
    db.Column('project_id', db.Integer, db.ForeignKey('project.id'), nullable=False),
    db.Column('skill_id', db.Integer, db.ForeignKey('skill.id'), nullable=False)
)

student_course = db.Table(
    'student_course', db.Model.metadata,
    db.Column('student_id', db.Integer, db.ForeignKey('student.id'), nullable=False),
    db.Column('course_id', db.Integer, db.ForeignKey('course.id'), nullable=False)
)

student_project = db.Table(
    'student_project', db.Model.metadata,
    db.Column('student_id', db.Integer, db.ForeignKey('student.id'), nullable=False),
    db.Column('project_id', db.Integer, db.ForeignKey('project.id'), nullable=False)
)

company_project = db.Table(
    'company_project', db.Model.metadata,
    db.Column('company_id', db.Integer, db.ForeignKey('company.id'), nullable=False),
    db.Column('project_id', db.Integer, db.ForeignKey('project.id'), nullable=False)
)

class Company(db.Model):
  __tablename__ = 'company'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String())
  url = db.Column(db.String())
  logo_url = db.Column(db.String())
  skills = db.relationship('Skill', secondary=company_skill, backref=db.backref('companies', lazy='dynamic'))
  projects = db.relationship('Project', secondary=company_project, backref=db.backref('companies', lazy='dynamic'))

  def __init__(self, name, url, logo_url):
    self.name = name
    self.url = url
    self.logo_url = logo_url

  def __repr__(self):
    return '<Company %r>' % self.name

class University(db.Model):
  __tablename__ = 'university'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String())
  country = db.Column(db.String())
  state = db.Column(db.String())
  city = db.Column(db.String())\

  def __init__(self, name, country, state, city):
    self.name = name
    self.country = country
    self.state = state
    self.city = city

  def __repr__(self):
    return '<University %r>' % self.name

class Professor(db.Model):
  __tablename__ = 'professor'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String())
  university_id = db.Column(db.Integer, db.ForeignKey('university.id'))
  university = db.relationship('University')

  def __init__(self, name, university):
    self.name = name
    self.university = university

  def __repr__(self):
    return '<Professor %r>' % self.name

class Course(db.Model):
  __tablename__ = 'course'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String())
  year = db.Column(db.CHAR(4))
  description = db.Column(db.Text)
  projects_start_date = db.Column(db.Date)
  projects_end_date = db.Column(db.Date)
  university_id = db.Column(db.Integer, db.ForeignKey('university.id'))
  professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'))
  university = db.relationship('University')
  professor = db.relationship('Professor')
  skills = db.relationship('Skill', secondary=course_skill, backref=db.backref('courses', lazy='dynamic'))
  # students = db.relationship('Student', secondary=student_skill, backref=db.backref('courses', lazy='dynamic'))

  def __init__(self, name, year, description, projects_start_date, projects_end_date, university, professor):
    self.name = name
    self.university = university
    self.description = description
    self.projects_start_date = projects_start_date
    self.projects_end_date = projects_end_date
    self.university = university
    self.professor = professor

  def __repr__(self):
    return '<Course %r>' % self.name

class Project(db.Model):
  __tablename__ = 'project'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  title = db.Column(db.String())
  summary = db.Column(db.Text)
  details = db.Column(db.Text)
  wordpress_url = db.Column(db.String())
  course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
  course = db.relationship('Course')
  skills = db.relationship('Skill', secondary=project_skill, backref=db.backref('projects', lazy='dynamic'))
  # students = db.relationship('Student', secondary=student_project, backref=db.backref('projects', lazy='dynamic'))
  # companies = db.relationship('Company', secondary=company_project, backref=db.backref('projects', lazy='dynamic'))

  def __init__(self, title, summary, details, wordpress_url, course):
    self.title =  title
    self.summary =  summary
    self.details =  details
    self.wordpress_url =  wordpress_url
    self.course =  course

  def __repr__(self):
    return '<Project %r>' % self.name

class Skill(db.Model):
  __tablename__ = 'skill'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String())
  category = db.Column(db.String())

  def __init__(self, name, category):
    self.title =  title
    self.category =  category

  def __repr__(self):
    return '<Skill %r>' % self.name

class Student(db.Model):
  __tablename__ = 'student'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String())
  dob = db.Column(db.Date)
  linkedin_url = db.Column(db.String())
  github_url = db.Column(db.String())
  stackoverflow_url = db.Column(db.String())
  start_date = db.Column(db.Date)
  university_id = db.Column(db.Integer, db.ForeignKey('university.id'))
  university = db.relationship('University')
  skills = db.relationship('Skill', secondary=student_skill, backref=db.backref('students', lazy='dynamic'))
  courses = db.relationship('Course', secondary=student_course, backref=db.backref('students', lazy='dynamic'))
  projects = db.relationship('Project', secondary=student_project, backref=db.backref('students', lazy='dynamic'))

  def __init__(self, name, dob, linkedin_url, github_url, stackoverflow_url, start_date, university):
    self.name = name
    self.dob = dob
    self.linkedin_url = linkedin_url
    self.github_url = github_url
    self.stackoverflow_url = stackoverflow_url
    self.start_date = start_date
    self.university = university

  def __repr__(self):
    return '<Student %r>' % self.name

class Account(db.Model):
  __tablename__ = 'account'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  username = db.Column(db.String())
  password = db.Column(db.String())
  role = db.Column(db.String())
  company_id = db.Column(db.Integer, db.ForeignKey('company.id'))
  company = db.relationship('Company')
  professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'))
  professor = db.relationship('Professor')
  student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
  student = db.relationship('Student')
  university_id = db.Column(db.Integer, db.ForeignKey('university.id'))
  university = db.relationship('University')

  def __init__(self, username, password, role, company, professor, student, university):
    self.username = username
    self.password = password
    self.role = role
    self.company = company
    self.professor = professor
    self.student = student
    self.university = university

  def __repr__(self):
    return '<Account %r>' % self.username
