#Bringing modules in
from flask import Flask, render_template, request, jsonify
from picamera2 import Picamera2, Preview
from time import sleep
import json

#setting up the camera
camera = Picamera2()

app = Flask(__name__)

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
#Where the Quiz data will be sent to the webserver
@app.route('/quiz2', methods=['GET', 'POST'])
def quiz2():

    if request.method == 'GET':
        print("GET")
    elif request.method == 'POST':
        data = request.form.get #getting the input from the form
        return jsonify('message', data)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
