from flask import Flask, render_template, request
from picamera2 import Picamera2, Preview
from time import sleep

app = Flask(__name__)

@app.route("/") #intial website page 
def home():
    return render_template('home1.html')

@app.route("/TRACKER")
def tracker():
    return render_template('tracker.html')

@app.route("/QUIZ")
def quiz():
    return render_template('quiz.html')

@app.route("/FALL")
def fall():
    return render_template('fall.html')

@app.route('/call-function')
def call_function():
    return feed()

def feed():
    camera = Picamera2()
    camera.start_preview(Preview.QTGL)
    sleep(2)
    camera.start()
    sleep(10)
    camera.close()
    return "Camera feed has been shown!"
    
if __name__ == "__main__":
    app.run(host="0.0.0.0")
