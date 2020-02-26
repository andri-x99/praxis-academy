from flask import Flask
from latihan_blue1 import simple_page
import urllib

app = Flask(__name__)
app.register_blueprint(simple_page)

print(app.url_map)
print()
print(simple_page.root_path)

with simple_page.open_resource('templates/css/bootstrap.css') as f:
    code = f.read()

url_for('admin.static', filename='style.css')