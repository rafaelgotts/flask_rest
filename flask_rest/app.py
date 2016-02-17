# -*- coding: utf-8 -*
from __future__ import unicode_literals

from flask import Flask
from flask_restful import Api

from flask_rest.tasks import BasicApi


def create_app(debug=False):
    app = Flask(__name__)
    app.debug = debug

    api = Api(app)
    api.add_resource(BasicApi, '/basic_api/<todo_id>')

    return app
