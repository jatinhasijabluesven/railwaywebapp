from flask import Flask 
from flask import render_template,request
from process_data import *

app = Flask(__name__)

"""
Load Home Page from template/home.html
"""
@app.route('/')
def home():
	return render_template('home.html')

"""
Load Search result Page from template/search.html
"""
@app.route('/search',methods = ['POST'])
def search():
	station_name = request.form.get('station_name')
	start_time = request.form.get('start_time')
	end_time = request.form.get('end_time')
	#function to retrieve the search results
	text,count = func(station_name , start_time , end_time)
	#render the data to prepare search results
	return render_template('search.html', html = '<div> Number of trains between interval is ' + str(count) + '</div>' + text) 

if __name__ == '__main__':
	app.run(debug=True)
