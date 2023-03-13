from flask import Flask, Blueprint, render_template, redirect
app = Flask(__name__)
bp = Blueprint('my_blueprint', __name__)

@app.route('/')
def main():
    return render_template('main.html')

@bp.route('/home')
def home():
    return render_template('home.html')

app.register_blueprint(bp)

app.run(debug=True)
