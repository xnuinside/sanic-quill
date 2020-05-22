import os

import json
from sanic import Sanic, Blueprint
from sanic_quill import add_editor
from sanic_jinja2 import SanicJinja2

app = Sanic(__name__)

jinja = SanicJinja2(app)

STATIC_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img')


current_dir = os.path.dirname(os.path.abspath(__file__))


@app.route('/', methods=['GET'])
async def index_route(request):
    return jinja.render(
        'index.html',
        request,
        posts=posts,
        categories=set([x['category'] for x in posts]))


def get_data(_id):
    """ this method defines logic to send to 'edit' form data of the object """
    for post in posts:
        if post['id'] == _id:
            post['title'] = post['title']
            post['content'] = post['body']
            post['preview'] = post['description']
            return post


def save_data(_id, data):
    """
        this method defines logic to save data from 'edit' form

        data comes like a dict with: content, content_preview and title fields,
        you need map it to your structure
    """
    for num, post in enumerate(posts):
        if post['id'] == _id:
            print('Update post')
            post['title'] = data['title']
            post['body'] = data['content']
            post['description'] = data['preview']
            break


add_editor(app, get_data, save_data, STATIC_FOLDER)


if __name__ == '__main__':
    with open(os.path.join(current_dir, 'posts.json'), 'r') as posts_file:
        posts = json.load(posts_file)

    app.run(host='0.0.0.0', port=5060)
