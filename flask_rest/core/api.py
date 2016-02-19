# -*- coding: utf-8 -*
from __future__ import unicode_literals

from flask_restful import Resource

class BaseApi(Resource):

    def get(self):
        raise NotImplementedError

    def post(self):
        raise NotImplementedError

    def put(self):
        raise NotImplementedError
