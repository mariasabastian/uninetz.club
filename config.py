import os
import json

# get service information from Bluemix
if 'VCAP_SERVICES' in os.environ:
  SERVICES = os.environ['VCAP_SERVICES']
else:
  with open('services.json') as services_file:    
    SERVICES = json.load(services_file)

with open('config.json') as config_file:    
  CONFIG = json.load(config_file)

DB_USER = SERVICES['user-provided'][0]['credentials']['username']
DB_PASSWORD = SERVICES['user-provided'][0]['credentials']['password']
DB_HOST = SERVICES['user-provided'][0]['credentials']['public_hostname']
DB_NAME = CONFIG['database']['name']
SQLALCHEMY_DATABASE_URI = "postgres://{username}:{password}@{host}/{database}"\
  .format(username=DB_USER, password=DB_PASSWORD, host=DB_HOST, database=DB_NAME)


SCHEMA = CONFIG['database']['schema']
DEVELOPMENT = True
DEBUG = True

SECRET_KEY = ''
STRIPE_API_KEY = ''