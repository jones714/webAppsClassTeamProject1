from flask import Flask, render_template
import util
import psycopg2
app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')
column_names = ["index","What country do you live in?","How old are you?","What is your gender?","To what extent do you feel FEAR due to the coronavirus?","To what extent do you feel ANXIOUS due to the coronavirus?","To what extent do you feel ANGRY due to the coronavirus?","To what extent do you feel HAPPY due to the coronavirus?","To what extent do you feel SAD due to the coronavirus?","Which emotion is having the biggest impact on you?","What makes you feel that way?","What brings you the most meaning during the coronavirus outbreak?","What is your occupation?"]

@app.route('/group1')
def test():
	result = util.group1()
	labels = util.cluster_user_data(result)
	return render_template('index.html', labels_html=labels, column_html=column_names, data_html=result)

@app.route('/group2')
def test2():
	result = util.group2()
	labels = util.cluster_user_data(result)
	return render_template('index.html', labels_html=labels, column_html=column_names, data_html=result)

@app.route('/group3')
def test3():
	result = util.group3()
	labels = util.cluster_user_data(result)
	return render_template('index.html', labels_html=labels, column_html=column_names, data_html=result)

@app.route('/group4')
def test4():
	result = util.group4()
	labels = util.cluster_user_data(result)
	return render_template('index.html', labels_html=labels, column_html=column_names, data_html=result)

@app.route('/group1_country')
def test5():
	result = util.group1_country()
	if len(result)>10:
		labels = util.cluster_user_data(result)
		result1=util.split_user_data(result, labels)
		for listss in result1:
			return render_template('index.html', labels_html=labels, column_html=column_names, data_html=listss)
	else:
		return ""


if __name__ == '__main__':
	# set debug mode
	app.debug = True
	# your local machine ip
	ip = '127.0.0.1'
	app.run(host=ip)
