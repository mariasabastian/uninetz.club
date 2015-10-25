from shared import ma
from data_models import Company, University, Professor, Course, Project, Skill, Student, Account

class SkillSchema(ma.ModelSchema):
  class Meta:
    model = Skill
  # students = ma.Nested('StudentSchema', many=True, exclude=('skills', ))
  # courses = ma.Nested('CourseSchema', many=True, exclude=('skills', ))
  # companies = ma.Nested('CompanySchema', many=True, exclude=('skills', ))
  # projects = ma.Nested('ProjectSchema', many=True, exclude=('skills', ))

skill_schema = SkillSchema()
skills_schema = SkillSchema(many=True)

class CompanySchema(ma.ModelSchema):
  class Meta:
    model = Company
  skills = ma.Nested('SkillSchema', many=True, exclude=('companies', ))
  projects = ma.Nested('ProjectSchema', many=True, exclude=('companies', ))

company_schema = CompanySchema()
companies_schema = CompanySchema(many=True)

class UniversitySchema(ma.ModelSchema):
  class Meta:
    model = University
  #professors = ma.Nested('ProfessorSchema', many=True, exclude=('university', ))
  #courses = ma.Nested('CourseSchema', many=True, exclude=('university', ))

university_schema = UniversitySchema()
universities_schema = UniversitySchema(many=True)

class ProfessorSchema(ma.ModelSchema):
  class Meta:
    model = Professor
  university = ma.Nested(UniversitySchema)
  #courses = ma.Nested('CourseSchema', many=True, exclude=('professor', ))

professor_schema = ProfessorSchema()
professors_schema = ProfessorSchema(many=True)
    
class CourseSchema(ma.ModelSchema):
  class Meta:
    model = Course
  university = ma.Nested(UniversitySchema)
  professor = ma.Nested(ProfessorSchema)
  skills = ma.Nested('SkillSchema', many=True, exclude=('courses', ))
  students = ma.Nested('StudentSchema', many=True, exclude=('courses', ))

course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)

class ProjectSchema(ma.ModelSchema):
  class Meta:
    model = Project
  course = ma.Nested(CourseSchema)
  skills = ma.Nested('SkillSchema', many=True, exclude=('projects', ))
  students = ma.Nested('StudentSchema', many=True, exclude=('projects', ))
  companies = ma.Nested('CompanySchema', many=True, exclude=('projects', ))

project_schema = ProjectSchema()
projects_schema = ProjectSchema(many=True)

class StudentSchema(ma.ModelSchema):
  class Meta:
    model = Student
  university = ma.Nested(UniversitySchema)
  skills = ma.Nested('SkillSchema', many=True, exclude=('students', 'companies', 'courses', 'projects'))
  courses = ma.Nested('CourseSchema', many=True, exclude=('students'))
  projects = ma.Nested('ProjectSchema', many=True, exclude=('students', 'course'))

student_schema = StudentSchema()
students_schema = StudentSchema(many=True)
    
class AccountSchema(ma.ModelSchema):
  class Meta:
    model = Account
  company = ma.Nested(CompanySchema)
  professor = ma.Nested(ProfessorSchema)
  student = ma.Nested(StudentSchema)
  university = ma.Nested(UniversitySchema)

account_schema = AccountSchema()
accounts_schema = AccountSchema(many=True)