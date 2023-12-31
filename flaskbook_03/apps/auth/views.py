from flask import Blueprint, render_template, flash, url_for, redirect, request  
from apps.app import db 
from apps.auth.forms import SignUpForm, LoginForm
from apps.crud.models import User 
from flask_login import login_user, logout_user 
auth = Blueprint(
    'auth', 
    __name__, 
    template_folder = 'templates', 
    static_folder = 'static'
)

@auth.route('/')
def index():
    return render_template('auth/index.html')


@auth.route('/signup', methods=['POST', 'GET'])
def signup():
    form = SignUpForm()
    
    if form.validate_on_submit():
        user = User(
            username=form.username.data, 
            email=form.email.data, 
            password=form.password.data 
        )
        
        if user.is_duplicate_email():
            flash('The E-Mail you entered is already registerd')
            return redirect(url_for('auth.signup')) 
        
        db.session.add(user)
        db.session.commit()
        
        login_user(user)
        next_ = request.args.get('next')
        
        if next_ is None or not next_.startswith('/'):
            print(next_)
            next_ = url_for('crud.users')   
        return redirect(next_)
    
    return render_template('auth/signup.html', form=form)


@auth.route('/login', methods=['POST', 'GET'])
def login():
    
    form = LoginForm() 
    
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
    
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(url_for('crud.users'))
        flash("The email address or password doesn't match.")
    
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
def logout():
    logout_user()
    
    return redirect(url_for('auth.login'))