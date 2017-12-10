from flask import Flask, render_template
from flask import request
from flask import make_response

app = Flask (__name__)

@app.route('/setcookies', methods = ['GET'])
def setcookie():
	name = request.args.get('name')
	age = request.args.get('age')
   
	resp = make_response(render_template('Task4.html'))
	resp.set_cookie('Name', name)
	resp.set_cookie('Age',age)
   
	return redirect("http://127.0.0.1:8080/getcookies")
   
app.run(debug=True,port=8080)