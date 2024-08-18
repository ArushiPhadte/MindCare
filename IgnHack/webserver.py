#MindCare
#Created by Arushi and Joy
#2024-08-18

#Bringing modules in
from flask import Flask, render_template, request, jsonify
from picamera2 import Picamera2, Preview
# flasksqlalchemy import SQLAlchemy
from time import sleep
from datetime import datetime,timedelta
import json

#setting up the camera
camera = Picamera2()

app = Flask(__name__)

#database
#app.config['SQLALCHEMYDATABASEURI']='sqlite:///symptoms.db
#db=SQLAlchemy(app)

#Functions to render the HTML for the site
@app.route("/") #intial website page for default
def home():
    return render_template('home1.html')

@app.route("/tracker")
def tracker():
    return render_template('tracker.html')

@app.route("/quiz")
def quiz():
    return render_template('quiz.html')

@app.route("/fall")
def fall():
    return render_template('fall.html')

#---CAMERA---
#calling a python script 
@app.route('/call-function')
def call_function():
    return feed()

#calling a python script
@app.route('/call-function2')
def call_function2():
    return leave()

#when camera is turned off 
def leave():
    camera.close()
    return "Camera feed has ended!"

#when camera is turned on
def feed():
    camera.start_preview(Preview.QTGL)
    sleep(2)
    camera.start()
    sleep(2)
    return "Camera feed has been shown!"
    
#---QUIZ---

#def foo():
 #   return bar
#Where the Quiz data will be sent to the webserver
@app.route('/quiz2', methods=['GET', 'POST'])
def quiz2():

    if request.method == 'GET':
        print("GET")
    elif request.method == 'POST':
        data = request.form #getting the input from the form
        
        s1 = data.get('S1')
        s2 = data.get('S2')  #
        s3 = data.get('S3')  
        s4 = data.get('S4')
        return f"Decreased Appetite?: {s1}  |  Fatigue?: {s2}  |  Low Energy Levels?: {s3}  |  Unusual Pains?: {s4}"


#Tracker


if __name__ == "__main__":
    app.run(host="0.0.0.0")
