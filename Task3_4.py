from flask import Flask, render_template
from flask import request
from flask import make_response

app = Flask (__name__)

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
   if request.method == 'POST':
   name = request.form['nm']
   age = request.form['age']
   
   resp = make_response(render_template('readcookie.html'))
   resp.set_cookie('Name', name)
   resp.set_cookie('Age',age)
   
   return resp
   
app.run(debug=True,port=8080)