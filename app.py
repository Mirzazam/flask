from flask import Flask, Blueprint, render_template

contact_us = Blueprint('contact', __name__, url_prefix='/contact')
@contact_us.route('/')
def contact():
    return render_template('contact-us.html')

payment = Blueprint('payments', __name__, url_prefix='/payments')
@payment.route('/')
def pay():
    return render_template('payments.html')

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

app.register_blueprint(contact_us)
app.register_blueprint(payment)

app.run(debug=True)
