from flask import render_template
from app.main import app

# Views
@app.route('/')
def index():

    return render_template('index.html')