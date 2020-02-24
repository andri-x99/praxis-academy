from flask.views import View
from flask import Flask
app = Flask('hehe')

class ShowUsers(View):

    def dispatch_request(self):
        users = User.query.all()
        return render_template('users.html', objects=users)

app.add_url_rule('/users/', view_func=ShowUsers.as_view('show_users'))

app.run(debug=True)