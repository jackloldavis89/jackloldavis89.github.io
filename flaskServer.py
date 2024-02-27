from flask import Flask, request, jsonify, send_from_directory, render_template, abort
from mongita import MongitaClientDisk
#set up ssh and pythonanywhere
app = Flask(__name__)
client = MongitaClientDisk()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/valentines')
def valentines():
    return render_template('valentines.html')

@app.route('/about_me')
def about_me():
    return render_template('about_me.html')

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

@app.route('/<page_name>')
def html_page(page_name):
    try:
        return send_from_directory('', page_name)
    except FileNotFoundError:
        abort(404)


app.run(debug=True)
