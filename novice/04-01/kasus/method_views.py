# https://pythonise.com/series/learning-flask/flask-api-methodview
# https://courses.prettyprinted.com/courses/168305/lectures/2520345
# Ctrl+D = menambahkan cursor menjadi lebih banyak dengan parameter huruf yang sama
# Alt + anak panah atas/bawah = mindah baris
# Robi
# modul request menggantikan browser / akses web / request web server / bisa dlakukan dengan modul requests / Import Requests / akses web melalui program
# venv kegunaannya mengethaui dependency projectnya apa aja

from flask.views import MethodView
from flask import Flask

app = Flask('dicoba')

class ExampleEndpoint(MethodView):
    """ Example of a class inheriting from flask.views.MethodView 

    All 5 request methods are available at /api/example/<entity>
    """
    def get(self):
        """ Responds to GET requests """
        return "Responding to a GET request"

    def post(self):
        """ Responds to POST requests """
        return "Responding to a POST request"

    def put(self):
        """ Responds to PUT requests """
        return "Responding to a PUT request"

    def patch(self):
        """ Responds to PATCH requests """
        return "Responding to a PATCH request"

    def delete(self):
        """ Responds to DELETE requests """
        return "Responding to a DELETE request"


app.add_url_rule("/api/example/", view_func=ExampleEndpoint.as_view("example_api"))

app.run(debug=True)