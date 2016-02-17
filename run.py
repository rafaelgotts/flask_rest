# -*- coding: utf-8 -*
from __future__ import unicode_literals

from flask_rest.app import create_app

app = create_app(debug=True)

if __name__ == '__main__':
    app.run()
