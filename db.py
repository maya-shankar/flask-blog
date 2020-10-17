import sqlite3
from werkzeug.exceptions import abort

def get_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_posts():
    conn = get_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return posts


def get_post(post_id):
    conn = get_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post


def put_post(title, content):
    conn = get_connection()
    conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                 (title, content))
    conn.commit()
    conn.close()


def edit_post(post_id, title, content):
    conn = get_connection()
    conn.execute('UPDATE posts SET title = ?, content = ?'
                 ' WHERE id = ?',
                 (title, content, post_id))
    conn.commit()
    conn.close()


def delete_post(post_id):
    conn = get_connection()
    conn.execute('DELETE FROM posts WHERE id = ?',
                 (post_id,))
    conn.commit()
    conn.close()

