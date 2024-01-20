from flask import Flask, render_template, request
import pyttsx3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speak')
def speak():
    engine = pyttsx3.init()
    # voice = engine.getProperty()
    engine.say("I will fuck you till end")
    engine.runAndWait()
    return render_template('index.html')