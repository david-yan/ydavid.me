from flask import Flask, render_template, redirect, send_from_directory

from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/assets/<path:path>')
def asset(path):
    return send_from_directory('assets', path)