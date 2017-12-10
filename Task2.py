# JSON objects handling
from flask import Flask
from flask import request
from flask import json
from flask import render_template
import requests

app = Flask(__name__)

@app.route('/authors')
def listofauthors():
	
	users = requests.get('https://jsonplaceholder.typicode.com/users').json()
	posts = requests.get('https://jsonplaceholder.typicode.com/posts').json()
	return render_template('Task2.html',users=users,posts=posts)
			
	return "Done"
	
app.run(debug = True,port=8080)