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


app = Flask(__name__)
app.config['SECRET_KEY'] = '2AZSMss3p05QpbcY2hBsJ'

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
        return redirect(url_for("contact_complete"))
    
    return render_template('contact_complete.html')


with app.test_request_context("/users?update=true"):
    print(request.args.get('updated'))
    print(url_for('index'))
    print(url_for('hello-endpoint', name='world'))
    print(url_for('show_name', name='AK', page='1'))
