from flask import Flask, render_template, redirect,url_for
from flask import request
from flask import make_response

app = Flask (__name__)

@app.route('/Task5')
def Task5():
    return render_template('Task5_1.html')
	
@app.route('/robot.txt')
def robot():
	return redirect(url_for('Task5'))

   
app.run(debug=True,port=8080)