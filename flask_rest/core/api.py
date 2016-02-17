# -*- coding: utf-8 -*
from __future__ import unicode_literals

from flask_restful import Resource, marshal_with

class BaseApi(Resource):
    resource_fields = {}

    @marshal_with(resource_fields)
    def get(self):
        raise NotImplementedError

    @marshal_with(resource_fields)
    def post(self):
        raise NotImplementedError

    @marshal_with(resource_fields)
    def put(self):
        raise NotImplementedError
