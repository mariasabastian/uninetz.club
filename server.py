import os
import logging
import json
import sys
from flask import Flask, render_template, jsonify
from flask.ext.bower import Bower

app = Flask(__name__)
Bower(app)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.DEBUG)

# get service information from Bluemix
if 'VCAP_SERVICES' in os.environ:
  services = os.environ['VCAP_SERVICES']
else:
  with open('services.json') as services_file:    
    services = json.load(services_file)

@app.route('/')
def Index():
  return render_template('index.html')

@app.route('/services')
def Services():
  return jsonify(services)

port = os.getenv('VCAP_APP_PORT', '5000')
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=int(port))