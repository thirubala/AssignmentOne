from flask import Flask, render_template
from flask import request
from flask import make_response

app = Flask (__name__)

@app.route('/getcookies')
def getcookies():
   name = request.cookies.get('name')
   age = request.cookies.get('age')
   return '<h1>Welcome '+name+'of age '+age+'</h1>'

app.run(debug=True,port=8080)