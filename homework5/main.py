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
	return render_template('index.html', column_html=column_names, data_html=result)

@app.route('/group2')
def test2():
	result = util.group2()
	return render_template('index.html', column_html=column_names, data_html=result)


@app.route('/group3')
def test3():
	result = util.group3()
	return render_template('index.html', column_html=column_names, data_html=result)

@app.route('/group4')
def test4():
	result = util.group4()
	return render_template('index.html', column_html=column_names, data_html=result)


@app.route('/country_group1')
def test6():
	#fetch list of countries and a dictionary of countries mapped with rows from csv for group1
	country, country_result = util.country_group1()
	result=util.group1()
	labels = util.cluster_user_data(result)
	x1=[]

	len_cluster=3
	j1=-1
	country1=[]
	for j  in range(len(country)):
		country_item=country[j]

		if len(country_result[country_item]) > 10:
			country1.append(country[j])
			result=util.group1()
			labels = util.cluster_user_data(country_result[country_item])
			j1=j1+1
			result1=util.split_user_data(country_result[country_item], labels)
			for i in range(3):
				#print(i)
				#print(j)
				x1.append([])
				x1[j1].append(result1[i])
				# print(j1)
				# print(i)
				# print(x1[j1][i])


	len_country1=len(country1)
	#print(len_country)
	#print(country)
	return render_template('index1.html', labels_html=labels, column_html=column_names, data_html=result1[0], x1=x1, len_country=len_country1, country=country1)

@app.route('/country_group2')
def test7():
	#fetch list of countries and a dictionary of countries mapped with rows from csv for group1
	country, country_result = util.country_group2()
	result=util.group2()
	labels = util.cluster_user_data(result)
	x1=[]

	len_cluster=3
	j1=-1
	country1=[]
	for j  in range(len(country)):
		country_item=country[j]

		if len(country_result[country_item]) > 10:
			country1.append(country[j])
			result=util.group2()
			labels = util.cluster_user_data(country_result[country_item])
			j1=j1+1
			result1=util.split_user_data(country_result[country_item], labels)
			for i in range(3):
				#print(i)
				#print(j)
				x1.append([])
				x1[j1].append(result1[i])



	len_country1=len(country1)
	#print(len_country)
	#print(country)
	return render_template('index1.html', labels_html=labels, column_html=column_names, data_html=result1[0], x1=x1, len_country=len_country1, country=country1)

@app.route('/country_group3')
def test8():
	#fetch list of countries and a dictionary of countries mapped with rows from csv for group1
	country, country_result = util.country_group3()
	result=util.group3()
	labels = util.cluster_user_data(result)
	x1=[]

	len_cluster=3
	j1=-1
	country1=[]
	for j  in range(len(country)):
		country_item=country[j]

		if len(country_result[country_item]) > 10:
			country1.append(country[j])
			result=util.group3()
			labels = util.cluster_user_data(country_result[country_item])
			j1=j1+1
			result1=util.split_user_data(country_result[country_item], labels)
			for i in range(3):
				#print(i)
				#print(j)
				x1.append([])
				x1[j1].append(result1[i])
				# print(j1)
				# print(i)
				# print(x1[j1][i])


	len_country1=len(country1)
	#print(len_country)
	#print(country)
	return render_template('index1.html', labels_html=labels, column_html=column_names, data_html=result1[0], x1=x1, len_country=len_country1, country=country1)


@app.route('/country_group4')
def test9():
	#fetch list of countries and a dictionary of countries mapped with rows from csv for group1
	country, country_result = util.country_group4()
	result=util.group4()
	labels = util.cluster_user_data(result)
	x1=[]

	len_cluster=3
	j1=-1
	country1=[]
	for j  in range(len(country)):
		country_item=country[j]

		if len(country_result[country_item]) > 10:
			country1.append(country[j])
			result=util.group4()
			labels = util.cluster_user_data(country_result[country_item])
			j1=j1+1
			result1=util.split_user_data(country_result[country_item], labels)
			for i in range(3):
				#print(i)
				#print(j)
				x1.append([])
				x1[j1].append(result1[i])
				# print(j1)
				# print(i)
				# print(x1[j1][i])


	len_country1=len(country1)
	#print(len_country)
	#print(country)
	return render_template('index1.html', labels_html=labels, column_html=column_names, data_html=result1[0], x1=x1, len_country=len_country1, country=country1)


if __name__ == '__main__':
	# set debug mode
	app.debug = True
	# your local machine ip
	ip = '127.0.0.1'
	app.run(host=ip)
