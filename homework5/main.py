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


@app.route('/country_group1')
def test6():
	country, country_result = util.country_group1()
	for country_item  in country:
		if len(country_result[country_item]) > 10:
			result=util.group1()
			labels = util.cluster_user_data(result)
			result1=util.split_user_data(country_result[country_item], labels)
			return render_template('index.html', labels_html=labels, column_html=column_names, data_html=result1)
		else:
			result=util.group1()
			labels = util.cluster_user_data(result)
			return render_template('index.html', labels_html=labels, column_html=column_names, data_html=result)




if __name__ == '__main__':
	# set debug mode
	app.debug = True
	# your local machine ip
	ip = '127.0.0.1'
	app.run(host=ip)
