#imporing libraries
from flask import Flask, Blueprint, render_template, redirect
#Flask syntax    
app = Flask(__name__)
bp = Blueprint('my_blueprint', __name__)

#creating route for index.html page
@app.route('/')
def index():
    return render_template('index.html')

#creating route for home page
@app.route('/home')
def home():
    return render_template('home.html')

app.register_blueprint(bp)

#function to run the app with debug mode which shows the changes made
app.run(debug=True)
