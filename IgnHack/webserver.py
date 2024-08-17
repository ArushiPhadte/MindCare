from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") #intial website page 
def home():
    return render_template('home1.html')

@app.route("/TRACKER")
def tracker():
        return render_template('tracker.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0")