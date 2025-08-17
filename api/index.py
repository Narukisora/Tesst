from flask import Flask, render_template
import os

# tell Flask where to find templates (important for Vercel’s file layout)
app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '../templates'))

@app.route("/")
def home():
    return render_template("index.html")
