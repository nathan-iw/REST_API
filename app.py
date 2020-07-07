from flask import Flask, request, render_template
import flask
import os
import sys
app = Flask(__name__,static_url_path = "/templates", static_folder = "templates")

    
@app.route("/")
def index():
    return "OOOOOoooopa! you've been HACKED! SKADOOOOSH"

# export FLASK_ENV=development
# export FLASK_APP=app.py

@app.route('/login', methods=['GET','POST'])
def login():
  img_url = flask.url_for('static', filename='gizmo.png')
  css_url = flask.url_for('static', filename='styles.css')
  if request.method == 'POST':
    #check user details from db
    username = request.form['broozername'] # correspond to the name
    password = request.form['passy']
    return render_template('loggdin.html',
      img_url=img_url, 
      name=username,
      css_url=css_url)
    
  elif request.method == 'GET':
    #serve login page
    return render_template('loggy_page.html',
      img_url=img_url, 
      css_url=css_url)

# def loggy_user():

# @app.route('/login/loggy')
# def serve_loggy_page():
#     return render_template('loggy_page.html')

# @app.route('/login/loggy')
# def login_user():
#     return render_template('loggy_page.html')