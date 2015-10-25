from sqlalchemy import *
from migrate import *

meta = MetaData()

# CREATE TABLE uninetz.UNIVERSITY (
#   ID SERIAL,
#   NAME VARCHAR(256) NOT NULL,
#   COUNTRY VARCHAR(256) NOT NULL,
#   STATE VARCHAR(256) NOT NULL,
#   CITY VARCHAR(256) NOT NULL,
#   PRIMARY KEY (ID)
# );

university = Table(
    'university', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(256), nullable=False),
    Column('country', String(256), nullable=False),
    Column('state', String(256), nullable=False),
    Column('city', String(256), nullable=False)
)

# CREATE TABLE uninetz.PROFESSOR (
#   ID SERIAL,
#   NAME VARCHAR(256) NOT NULL,
#   UNIVERSITY_ID INT NOT NULL,
#   FOREIGN KEY (UNIVERSITY_ID) REFERENCES UNIVERSITY(ID),
#   PRIMARY KEY (ID)
# );

professor = Table(
    'professor', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(256), nullable=False),
    Column('university_id', Integer, nullable=False)
)

# CREATE TABLE uninetz.COURSE (
#   ID SERIAL,
#   NAME VARCHAR(256) NOT NULL,
#   YEAR CHAR(4) NOT NULL,
#   DESCRIPTION TEXT,
#   PROJECTS_START_DATE DATE NOT NULL,
#   PROJECTS_END_DATE DATE NOT NULL,
#   UNIVERSITY_ID INT NOT NULL,
#   PROFESSOR_ID INT NOT NULL,
#   FOREIGN KEY (UNIVERSITY_ID) REFERENCES UNIVERSITY(ID),
#   FOREIGN KEY (PROFESSOR_ID) REFERENCES PROFESSOR(ID),
#   PRIMARY KEY (ID)
# );

course = Table(
    'course', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(256), nullable=False),
    Column('year', CHAR(4), nullable=False),
    Column('description', Text, nullable=True),
    Column('projects_start_date', Date, nullable=False),
    Column('projects_end_date', Date, nullable=False),
    Column('university_id', Integer, nullable=False),
    Column('professor_id', Integer, nullable=False)
)

# CREATE TABLE uninetz.PROJECT (
#   ID SERIAL,
#   TITLE VARCHAR(256) NOT NULL,
#   SUMMARY TEXT,
#   DETAILS TEXT,
#   BLOG_URL VARCHAR(256),
#   COURSE_ID INT NOT NULL,
#   FOREIGN KEY (COURSE_ID) REFERENCES COURSE(ID),
#   PRIMARY KEY (ID)
# );

project = Table(
    'project', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('title', String(256), nullable=False),
    Column('summary', Text, nullable=True),
    Column('details', Text, nullable=True),
    Column('wordpress_url', String(256), nullable=True),
    Column('course_id', Integer, nullable=False)
)

# CREATE TABLE uninetz.COMPANY (
#   ID SERIAL,
#   NAME VARCHAR(256) NOT NULL,
#   URL VARCHAR(256),
#   LOGO_URL VARCHAR(256),
#   PRIMARY KEY (ID)
# );

company = Table(
    'company', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(256), nullable=False),
    Column('url', String(256), nullable=True),
    Column('logo_url', String(256), nullable=True)
)

# CREATE TABLE uninetz.SKILL (
#   ID SERIAL,
#   NAME VARCHAR(256) NOT NULL,
#   CATEGORY VARCHAR(256) NOT NULL,
#   PRIMARY KEY (ID)
# );

skill = Table(
    'skill', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(256), nullable=False),
    Column('category', String(256), nullable=False)
)

# CREATE TABLE uninetz.STUDENT (
#   ID SERIAL,
#   NAME VARCHAR(256) NOT NULL,
#   DOB DATE NOT NULL,
#   LINKEDIN_URL VARCHAR(256),
#   GITHUB_URL VARCHAR(256),
#   STACKOVERFLOW_URL VARCHAR(256),
#   START_DATE DATE NOT NULL,
#   UNIVERSITY_ID INT NOT NULL,
#   FOREIGN KEY (UNIVERSITY_ID) REFERENCES UNIVERSITY(ID),
#   PRIMARY KEY (ID)
# );

student = Table(
    'student', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(256), nullable=False),
    Column('dob', Date, nullable=False),
    Column('linkedin_url', String(256), nullable=True),
    Column('github_url', String(256), nullable=True),
    Column('stackoverflow_url', String(256), nullable=True),
    Column('start_date', Date, nullable=False),
    Column('university_id', Integer, nullable=False)
)

# CREATE TABLE uninetz.ACCOUNT (
#   ID SERIAL,
#   USERNAME VARCHAR(256) NOT NULL,
#   PASSWORD CHAR(60) NOT NULL,
#   ROLE VARCHAR(64) NOT NULL,
#   COMPANY_ID INT,
#   STUDENT_ID INT,
#   PROFESSOR_ID INT,
#   FOREIGN KEY (COMPANY_ID) REFERENCES COMPANY(ID),
#   FOREIGN KEY (STUDENT_ID) REFERENCES STUDENT(ID),
#   FOREIGN KEY (PROFESSOR_ID) REFERENCES PROFESSOR(ID)
# );

account = Table(
    'account', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('username', String(256), nullable=False),
    Column('password', String(256), nullable=False),
    Column('role', String(16), nullable=False),
    Column('company_id', Integer, nullable=True),
    Column('professor_id', Integer, nullable=True),
    Column('student_id', Integer, nullable=True),
    Column('university_id', Integer, nullable=True)
)

# CREATE TABLE uninetz.STUDENT_SKILL (
#   RATING INT NOT NULL,
#   STUDENT_ID INT NOT NULL,
#   SKILL_ID INT NOT NULL,
#   FOREIGN KEY (STUDENT_ID) REFERENCES STUDENT(ID),
#   FOREIGN KEY (SKILL_ID) REFERENCES SKILL(ID)
# );

student_skill = Table(
    'student_skill', meta,
    Column('rating', Integer, nullable=False),
    Column('student_id', Integer, nullable=False),
    Column('skill_id', Integer, nullable=False)
)

# CREATE TABLE uninetz.COURSE_SKILL (
#   STUDENT_ID INT NOT NULL,
#   SKILL_ID INT NOT NULL,
#   FOREIGN KEY (STUDENT_ID) REFERENCES STUDENT(ID),
#   FOREIGN KEY (SKILL_ID) REFERENCES SKILL(ID)
# );

course_skill = Table(
    'course_skill', meta,
    Column('course_id', Integer, nullable=False),
    Column('skill_id', Integer, nullable=False)
)

# CREATE TABLE uninetz.COMPANY_SKILL (
#   COMPANY_ID INT NOT NULL,
#   SKILL_ID INT NOT NULL,
#   FOREIGN KEY (COMPANY_ID) REFERENCES COMPANY(ID),
#   FOREIGN KEY (SKILL_ID) REFERENCES SKILL(ID)
# );

company_skill = Table(
    'company_skill', meta,
    Column('company_id', Integer, nullable=False),
    Column('skill_id', Integer, nullable=False)
)

# CREATE TABLE uninetz.PROJECT_SKILL (
#   PROJECT_ID INT NOT NULL,
#   SKILL_ID INT NOT NULL,
#   FOREIGN KEY (PROJECT_ID) REFERENCES PROJECT(ID),
#   FOREIGN KEY (SKILL_ID) REFERENCES SKILL(ID)
# );

project_skill = Table(
    'project_skill', meta,
    Column('project_id', Integer, nullable=False),
    Column('skill_id', Integer, nullable=False)
)

# CREATE TABLE uninetz.STUDENT_COURSE (
#   STUDENT_ID INT NOT NULL,
#   COURSE_ID INT NOT NULL,
#   FOREIGN KEY (STUDENT_ID) REFERENCES STUDENT(ID),
#   FOREIGN KEY (COURSE_ID) REFERENCES COURSE(ID)
# );

student_course = Table(
    'student_course', meta,
    Column('student_id', Integer, nullable=False),
    Column('course_id', Integer, nullable=False)
)

# CREATE TABLE uninetz.STUDENT_PROJECT (
#   STUDENT_ID INT NOT NULL,
#   PROJECT_ID INT NOT NULL,
#   FOREIGN KEY (STUDENT_ID) REFERENCES STUDENT(ID),
#   FOREIGN KEY (PROJECT_ID) REFERENCES PROJECT(ID)
# );

student_project = Table(
    'student_project', meta,
    Column('student_id', Integer, nullable=False),
    Column('project_id', Integer, nullable=False)
)

# CREATE TABLE uninetz.COMPANY_PROJECT (
#   ACCEPTED BOOLEAN,
#   COMPANY_ID INT NOT NULL,
#   PROJECT_ID INT NOT NULL,
#   FOREIGN KEY (COMPANY_ID) REFERENCES COMPANY(ID),
#   FOREIGN KEY (PROJECT_ID) REFERENCES PROJECT(ID)
# );

company_project = Table(
    'company_project', meta,
    Column('company_id', Integer, nullable=False),
    Column('project_id', Integer, nullable=False)
)

def upgrade(migrate_engine):
    meta.bind = migrate_engine

    university.create()
    professor.create()
    course.create()
    project.create()
    company.create()
    skill.create()
    student.create()
    account.create()
    student_skill.create()
    course_skill.create()
    company_skill.create()
    project_skill.create()
    student_course.create()
    student_project.create()
    company_project.create()
    
    # TABLE: professor
    ForeignKeyConstraint([professor.c.university_id], [university.c.id]).create()
    Index('professor_university_ix', professor.c.university_id).create()

    # TABLE: course
    ForeignKeyConstraint([course.c.university_id], [university.c.id]).create()
    Index('course_university_ix', course.c.university_id).create()

    ForeignKeyConstraint([course.c.professor_id], [professor.c.id]).create()
    Index('course_professor_ix', course.c.professor_id).create()

    # TABLE: project
    ForeignKeyConstraint([project.c.course_id], [course.c.id]).create()
    Index('project_course_ix', project.c.course_id).create()
    
    # TABLE: student
    ForeignKeyConstraint([student.c.university_id], [university.c.id]).create()
    Index('student_university_ix', student.c.university_id).create()

    # TABLE: account
    ForeignKeyConstraint([account.c.company_id], [company.c.id]).create()
    Index('account_company_ix', account.c.company_id).create()

    ForeignKeyConstraint([account.c.professor_id], [professor.c.id]).create()
    Index('account_professor_ix', account.c.professor_id).create()

    ForeignKeyConstraint([account.c.student_id], [student.c.id]).create()
    Index('account_student_ix', account.c.student_id).create()

    ForeignKeyConstraint([account.c.university_id], [university.c.id]).create()
    Index('account_university_ix', account.c.university_id).create()

    # TABLE: student_skill
    ForeignKeyConstraint([student_skill.c.student_id], [student.c.id]).create()
    Index('student_skill_student_ix', student_skill.c.student_id).create()

    ForeignKeyConstraint([student_skill.c.skill_id], [skill.c.id]).create()
    Index('student_skill_skill_ix', student_skill.c.skill_id).create()
    
    # TABLE: course_skill
    ForeignKeyConstraint([course_skill.c.course_id], [course.c.id]).create()
    Index('course_skill_course_ix', course_skill.c.course_id).create()

    ForeignKeyConstraint([course_skill.c.skill_id], [skill.c.id]).create()
    Index('course_skill_skill_ix', course_skill.c.skill_id).create()
    
    # TABLE: company_skill
    ForeignKeyConstraint([company_skill.c.company_id], [company.c.id]).create()
    Index('company_skill_company_ix', company_skill.c.company_id).create()

    ForeignKeyConstraint([company_skill.c.skill_id], [skill.c.id]).create()
    Index('company_skill_skill_ix', company_skill.c.skill_id).create()
    
    # TABLE: project_skill
    ForeignKeyConstraint([project_skill.c.project_id], [project.c.id]).create()
    Index('project_skill_project_ix', project_skill.c.project_id).create()

    ForeignKeyConstraint([project_skill.c.skill_id], [skill.c.id]).create()
    Index('project_skill_skill_ix', project_skill.c.skill_id).create()
    
    # TABLE: student_course
    ForeignKeyConstraint([student_course.c.student_id], [student.c.id]).create()
    Index('student_course_student_ix', student_course.c.student_id).create()

    ForeignKeyConstraint([student_course.c.course_id], [course.c.id]).create()
    Index('student_course_course_ix', student_course.c.course_id).create()
    
    # TABLE: student_project
    ForeignKeyConstraint([student_project.c.student_id], [student.c.id]).create()
    Index('student_project_student_ix', student_project.c.student_id).create()

    ForeignKeyConstraint([student_project.c.project_id], [project.c.id]).create()
    Index('student_project_project_ix', student_project.c.project_id).create()
    
    # TABLE: company_project
    ForeignKeyConstraint([company_project.c.company_id], [company.c.id]).create()
    Index('company_project_company_ix', company_project.c.company_id).create()

    ForeignKeyConstraint([company_project.c.project_id], [project.c.id]).create()
    Index('company_project_project_ix', company_project.c.project_id).create()


def downgrade(migrate_engine):
    meta.bind = migrate_engine

    ForeignKeyConstraint(columns=[company_project.c.project_id], refcolumns=[project.c.id]).drop()
    ForeignKeyConstraint(columns=[company_project.c.company_id], refcolumns=[company.c.id]).drop()
    ForeignKeyConstraint(columns=[student_project.c.project_id], refcolumns=[project.c.id]).drop()
    ForeignKeyConstraint(columns=[student_project.c.student_id], refcolumns=[student.c.id]).drop()
    ForeignKeyConstraint(columns=[student_course.c.course_id], refcolumns=[course.c.id]).drop()
    ForeignKeyConstraint(columns=[student_course.c.student_id], refcolumns=[student.c.id]).drop()
    ForeignKeyConstraint(columns=[student_course.c.course_id], refcolumns=[course.c.id]).drop()
    ForeignKeyConstraint(columns=[student_course.c.student_id], refcolumns=[student.c.id]).drop()
    ForeignKeyConstraint(columns=[project_skill.c.skill_id], refcolumns=[skill.c.id]).drop()
    ForeignKeyConstraint(columns=[project_skill.c.project_id], refcolumns=[project.c.id]).drop()
    ForeignKeyConstraint(columns=[company_skill.c.skill_id], refcolumns=[skill.c.id]).drop()
    ForeignKeyConstraint(columns=[company_skill.c.company_id], refcolumns=[company.c.id]).drop()
    ForeignKeyConstraint(columns=[course_skill.c.skill_id], refcolumns=[skill.c.id]).drop()
    ForeignKeyConstraint(columns=[course_skill.c.course_id], refcolumns=[course.c.id]).drop()
    ForeignKeyConstraint(columns=[student_skill.c.skill_id], refcolumns=[skill.c.id]).drop()
    ForeignKeyConstraint(columns=[student_skill.c.student_id], refcolumns=[student.c.id]).drop()
    ForeignKeyConstraint(columns=[account.c.university_id], refcolumns=[university.c.id]).drop()
    ForeignKeyConstraint(columns=[account.c.student_id], refcolumns=[student.c.id]).drop()
    ForeignKeyConstraint(columns=[account.c.professor_id], refcolumns=[professor.c.id]).drop()
    ForeignKeyConstraint(columns=[account.c.company_id], refcolumns=[company.c.id]).drop()
    ForeignKeyConstraint(columns=[student.c.university_id], refcolumns=[university.c.id]).drop()
    ForeignKeyConstraint(columns=[project.c.course_id], refcolumns=[course.c.id]).drop()
    ForeignKeyConstraint(columns=[course.c.professor_id], refcolumns=[professor.c.id]).drop()
    ForeignKeyConstraint(columns=[course.c.university_id], refcolumns=[university.c.id]).drop()
    ForeignKeyConstraint(columns=[professor.c.university_id], refcolumns=[university.c.id]).drop()

    company_project.drop()
    student_project.drop()
    student_course.drop()
    project_skill.drop()
    company_skill.drop()
    course_skill.drop()
    student_skill.drop()
    account.drop()
    student.drop()
    skill.drop()
    company.drop()
    project.drop()
    course.drop()
    professor.drop()
    university.drop()