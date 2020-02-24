from flask import request

@app.route("/api/example/<entity>", methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
def api_example_all_methods(entity):
    """ Request method logic handled inside the function """
    if request.method == "GET":
        """ Respond to the GET request """
        return "Responding to a GET request"
    if request.method == "POST":
        """ Respond to the POST request """
        return "Responding to a POST request"
    if request.method == "PUT":
        """ Respond to the PUT request """
        return "Responding to a PUT request"
    if request.method == "PATCH":
        """ Respond to the PATCH request """
        return "Responding to a PATCH request"
    if request.method == "DELETE":
        """ Respond to the DELETE request """
        return "Responding to a DELETE request"