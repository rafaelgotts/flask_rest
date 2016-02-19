# -*- coding: utf-8 -*
from __future__ import unicode_literals

from flask_restful import reqparse, marshal_with
from flask_rest.core.api import BaseApi


"""
    The reqparse receive and parser the args sent to the api.
    But, like the python argparse, it's a little limited.
"""
parser = reqparse.RequestParser()
parser.add_argument('task', type=str)


"""
    Representation of the fields in the resource
    this fields are serialized on **reponse**
"""
from flask_restful import fields
basic_fields = {
    'task': fields.String,
    'task_id': fields.Integer
}

"""
    Representation of a database
"""
TODOS = {}

class BasicApi(BaseApi):
    # So creative han?
    resource_fields=basic_fields

    @marshal_with(basic_fields)
    def post(self, todo_id):
        """
            Receive and serialize the fields.
            If they cannot parse, then an error is returned
        """
        parsed_args = parser.parse_args()
        task_description = parsed_args['task']

        """ Simulates the database
        """
        TODOS[todo_id] = {'task': task_description}

        """
            Now, i will create the data for the response
            and the marshal_with will serialize based on
            dict basic_fields.
        """
        data = {'task_id': todo_id, 'task': task_description}

        return data, 201

    def get(self, todo_id):
        return TODOS[todo_id]
