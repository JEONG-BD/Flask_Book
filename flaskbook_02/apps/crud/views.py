from flask import Blueprint, render_template, url_for, redirect
from apps.app import db 
from apps.crud.models import User 
from apps.crud.forms import UserForm

crud = Blueprint(
    'crud', 
    __name__, 
    template_folder = 'templates',
    static_folder = 'static', 
)


@crud.route('/')
def index():
    return render_template('crud/index.html')


@crud.route('/sql')
def sql():
    db.session.query(User).all()
    return 'Check your console logs'


@crud.route('/users/news', methods=["GET", "POST"])
def create_user():
    form = UserForm()

    if form.validate_on_submit():
        user = User(
            username = form.username.data, 
            email = form.email.data,
            password = form.password.data 
        )
        print(user)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for("crud.users"))
    return render_template('crud/create.html', form=form)

