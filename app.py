import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect

import db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'rGfS1AGyCIkOQN5inOgYNtfhAtYbQ5psY9D6g4d7CcZeHwFcUcLHPw=='


@app.route('/')
def index():
    posts = db.get_posts()
    return render_template('index.html', posts=posts)


@app.route('/post/<int:post_id>', methods=('GET', 'PUT', 'DELETE'))
def post(post_id):
    post = db.get_post(post_id)
    if request.method == 'GET':
        return render_template('post.html', post=post)

    elif request.method == 'PUT':
        title = request.form['title']
        content = request.form['content']

        if not (title and content):
            flash('Title and content are required!')
        else:
            db.edit_post(post_id, title, content)
            return render_template('post.html', post=post)

    elif request.method == 'DELETE':
        post = db.get_post(post_id)
        db.delete_post(post_id)
        flash(f"Post {post['title']} was successfully deleted")
        return redirect(url_for('index'))
    

@app.route('/post', methods=('POST',))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not (title and content):
            flash('Title and content are required!')
        else:
            db.put_post(title, content)
            return redirect(url_for('index'))

    return render_template('create.html')


@app.route('/about')
def about():
    return render_template('about.html')
