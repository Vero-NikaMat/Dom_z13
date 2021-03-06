import json

from flask import Flask, request, render_template, send_from_directory, abort
from functions import get_data, open_file, kakaya_to_funksia, add_post

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)


@app.route("/")
def page_index():
    tags = get_data(open_file('posts.json'))
    return render_template("index.html", tags=tags)


@app.route("/tag")
def page_tag():
    tag = request.args.get("tag")
    if not tag:
        abort(400)
    data = open_file('posts.json')
    posts = kakaya_to_funksia(data, tag)
    return render_template('post_by_tag.html', posts=posts, tag=tag)

@app.route("/post", methods=["GET", "POST"])
def page_post_create():
    if request.method == 'GET':
        return render_template('post_form.html')

    content = request.form.get('content')
    picture = request.files.get('picture')
    if not content or not picture:
        abort(400)
    path = f'{UPLOAD_FOLDER}/{picture.filename}'
    post = {
        'content': content,
        'pic' : f'/{path}'
    }

    picture.save(path)
    add_post(POST_PATH, post)
    return render_template('post_uploaded.html', post=post)


@app.route("/uploads/images/<path>")
def static_dir(path):
    return send_from_directory("uploads/images", path)


app.run(debug=True)

