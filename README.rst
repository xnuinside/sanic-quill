sanic-quill
-----------

Sanic-quill is a port of Flask-quill (https://github.com/drewdru/flask-quill/) to Sanic ecosystem. (wtforms widget for quill.js editor (https://github.com/quilljs/quill))

Quill.js is a modern WYSIWYG editor built for compatibility and extensibility.



To add routes with edit form:

from sanic_quill import add_editor

editor will be able on the route /edit

How to use
----------

Check sample in 'examples'.


To add  WYSIWYG editor to edit any data/fields you need to define 2 methods:

- get_data (used by editor to get information for model to edit in form)
- save_data (used by editor to save changes from the form)

Editor expect 3 fields in data:

    -  'title',
    -  'body',
    -  'preview'

.. code-block:: python



    from sanic_quill import add_editor

    ...

    # your Sanic app code
    # with defining app = Sanic()

    ...

    def get_data(_id):
        """ this method defines logic to send to 'edit' form data of the object """
        for post in posts:
            if post['id'] == _id:
                post['title'] = post['title']
                post['content'] = post['text']
                post['preview'] = post['preview']
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
                post['text'] = data['content']
                post['description'] = data['preview']
                break

    add_editor(app, get_data, save_data)

After that you will have routes '/edit?'id=$id_of_your_data_item_to_edit

Also you can define a path where to save an images and route that will be used to serve uploaded images by default it is '/img':

.. code-block:: python

    add_editor(app, get_data, save_data, img_folder="/path/for/images", route_for_img='/custom_route')

