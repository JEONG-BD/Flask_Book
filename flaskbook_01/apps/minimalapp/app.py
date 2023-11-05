import os 
import logging
from flask_mail import Mail, Message 
from email_validator import validate_email, EmailNotValidError 
from flask import (
    Flask, 
    render_template, 
    url_for, 
    request, 
    redirect, 
    g, 
    flash, 
    current_app
)
from flask_debugtoolbar import DebugToolbarExtension 


app = Flask(__name__)
app.config['SECRET_KEY'] = '2AZSMss3p05QpbcY2hBsJ'
app.logger.setLevel(logging.DEBUG)
app.logger.critical('fatal error')
app.logger.error('error')
app.logger.warning('warning')
app.logger.info('info')
app.logger.debug('debug')
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# Mail 
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER')
app.config['MAIL_PORT'] = os.environ.get('MAIL_PORT')
# app.config['MAIL_USE_TLS'] = os.environ.get('MAIL_USE_TLS')
app.config['MAIL_USE_SSL'] = os.environ.get('MAIL_USE_SSL')
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER')
mail = Mail(app)
toolbar = DebugToolbarExtension(app)

@app.route('/')
def index():
    return 'Hello Flask Book'

# Step0
# @app.route('/hello', 
#            methods=['GET'],
#            endpoint="hello-endpoint")
#def hello(name):
#    return 'Hello World'

# Step1 
# @app.route('/hello/<name>', 
#            methods=['GET', 'POST'],
#            endpoint="hello-endpoint")
# def hello(name):
#     return f'Hello {name}!'


@app.route('/hello/<name>', 
           methods=['GET', 'POST'],
           endpoint='hello-endpoint')
def hello(name):
    return f'Hello {name}!'


@app.route('/name/<name>')
def show_name(name):
    return render_template('index.html', name=name)


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/contact/complete', methods=['GET', 'POST'])
def contact_complete():   
    
    if request.method == 'POST':        
        
        username = request.form['username']
        email = request.form['email']
        description = request.form['description']
        is_valid = True 

        if not username:
            flash('The User Name is required')
            is_valid = False 
        
        if not email :
            flash('The E-Mail is required')
            is_valid = False 
        
        try : 
            validate_email(email)
        except EmailNotValidError: 
            flash('Please enter the format of your email address ')
            is_valid = False 
        
        if not description : 
            flash("The Description is required")
            is_valid = False 
        
        if not is_valid:
            print("=======")
            return redirect(url_for('contact'))
        
        flash('Thank you for your inquiry')

        send_email(email, 
                   "Thank you", 
                   "contact_mail", 
                   username=username, 
                   description=description)
        return redirect(url_for("contact_complete"))
    
    return render_template('contact_complete.html')

def send_email(to, subject, template, **kwargs):
    msg = Message(subject, recipients=[to])
    msg.body = render_template(template + ".txt", **kwargs)
    msg.html = render_template(template + ".html", **kwargs)
    mail.send(msg)
    
with app.test_request_context("/users?update=true"):
    print(request.args.get('updated'))
    print(url_for('index'))
    print(url_for('hello-endpoint', name='world'))
    print(url_for('show_name', name='AK', page='1'))
