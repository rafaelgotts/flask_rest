# -*- coding: utf-8 -*
from __future__ import unicode_literals

from flask_restful import reqparse
from flask_rest.core.api import BaseApi

parser = reqparse.RequestParser()
parser.add_argument('task')


"""
    Representation of the fields in the resource
"""
from flask_restful import fields
basic_fields = {
    'task': fields.String,
    'uri': fields.Url('basic_api')
}

"""
    Representation of a database
"""
TODOS = {}

class BasicApi(BaseApi):
    # So creative han?
    resource_fields=basic_fields

    def post(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201

    def get(self, todo_id):
        return TODOS[todo_id]
