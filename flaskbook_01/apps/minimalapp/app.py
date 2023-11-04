from flask import Flask, render_template, url_for, request, redirect    

app = Flask(__name__)


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
        return redirect(url_for("contact_complete"))
    return render_template('contact_complete.html')

with app.test_request_context("/users?update=true"):
    print(request.args.get('updated'))
    print(url_for('index'))
    print(url_for('hello-endpoint', name='world'))
    print(url_for('show_name', name='AK', page='1'))
