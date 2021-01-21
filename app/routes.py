import datetime

from flask import Flask, render_template, redirect, send_from_directory, url_for
from flask_login import current_user, login_user, logout_user
from werkzeug.security import generate_password_hash

from app import app
from app.forms import LoginForm, PostForm
from app.models import Admin, Post

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/post')
def post():
    return render_template('post.html')

@app.route('/admin')
def admin():
    if not current_user.is_authenticated:
        login_form = LoginForm()
        return render_template('login.html', form=login_form)

    post_form = PostForm()
    return render_template('admin.html', post_form=post_form)

@app.route('/admin_login', methods=['POST'])
def admin_login():
    if current_user.is_authenticated:
        return redirect(url_for('admin'))

    login_form = LoginForm()
    if login_form.validate_on_submit():
        app.logger.info('Attempted admin login with password: {}, time: {}'.format(
            login_form.password.data, datetime.datetime.now()
        ))
        if login_form.password.data == app.config['ADMIN_KEY']:
            user = Admin()
            login_user(user, remember=True)
    return redirect(url_for('admin'))

@app.route('/admin_logout', methods=['POST'])
def admin_logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/assets/<path:path>')
def asset(path):
    return send_from_directory('assets', path)