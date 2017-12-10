from flask import Flask, render_template, redirect,url_for
from flask import request
from flask import make_response

app = Flask (__name__)

@app.route('/html')
def render_img():
    return render_template('Task6.html')

app.run(debug=True,port=8080)