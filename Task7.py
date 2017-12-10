from flask import Flask, render_template
from flask import request
from flask import make_response

app = Flask (__name__)

@app.route('/input')
def input():
	resp = make_response(render_template('Task7.html'))
	
	return "Receiving Inputs"

@app.route('/result',methods = "Post")
def print_input():
	
	name = request.form('name')
	age = request.form('age')
   
	return "Name:"+name+" Age:"+age
   	
app.run(debug=True,port=8080)