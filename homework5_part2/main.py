from flask import Flask, render_template
import util
import psycopg2
import json
app = Flask(__name__)


@app.route('/')
def index():
	return render_template('home.html')
column_names = ["index","What country do you live in?","How old are you?","What is your gender?","To what extent do you feel FEAR due to the coronavirus?","To what extent do you feel ANXIOUS due to the coronavirus?","To what extent do you feel ANGRY due to the coronavirus?","To what extent do you feel HAPPY due to the coronavirus?","To what extent do you feel SAD due to the coronavirus?","Which emotion is having the biggest impact on you?","What makes you feel that way?","What brings you the most meaning during the coronavirus outbreak?","What is your occupation?"]




SURVEY_DATA_COUNTRY = util.allcountryy()

@app.route('/api/query_survey_results/<country_name>', methods=['GET'])
def query_survey_results(country_name=''):

	c,dc=util.country_group1()
	print(dc)
	SURVEY_DATA_COUNTRY=list(map(util.mapcountry, c))
	print(SURVEY_DATA_COUNTRY)
	if country_name in SURVEY_DATA_COUNTRY:
		if country_name == 'United States of America':
			country_key='USA'

		elif country_name=='United Kingdom':
			country_key='UK'
		elif country_name=='Spain':
			country_key='spain'
		elif country_name=='Ireland':
			country_key='Ireland l'
		else:
			country_key=country_name
		survey_query_data = {
					'user_data': dc[country_key]
							}

# {country: USA, group: group1,  cluster0: [], cluster1: [], cluster2: []}


	else:
		survey_query_data = {'user_data':[country_name+" does not have any survey data"]}
	print(survey_query_data)
	return json.dumps(survey_query_data)

# new part
# country = util.allcountry()
# print(country)

@app.route('/mapdata')
def indexdm():

	return render_template('indexdm.html')


#end new part

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
	#print(country_result)
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
	print(x1)
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

	print(x1)


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
	print(x1)

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

	print(x1)
	len_country1=len(country1)
	#print(len_country)
	#print(country)
	return render_template('index1.html', labels_html=labels, column_html=column_names, data_html=result1[0], x1=x1, len_country=len_country1, country=country1)

#####


	#fetch list of countries and a dictionary of countries mapped with rows from csv for group1
@app.route('/api/query_survey_results2/United States of America', methods=['GET'])
def query_survey_results2(country_name=''):

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
		group3=x1
		#print(group3)

		country, country_result = util.country_group1()
		#print(country_result)
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
		group1=x1
		#print(group1)
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

		group2=x1
		#print(group2)
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

		group4=x1
		#print(group4)
		dictionary_usa={'country':['Unites States Of America']}
		dictionary_romania={'country':['Romania']}
		dictionary_switzerland={'country':['Switzerland']}
		for i in range(2):
		   for j in range(3):
		       if((group1[i][j][1][1]).strip()=='USA'):
		           dictionary_usa['group1'+'cluster'+str(j)]=[group1[i][j]]
		       else:
		           dictionary_romania['group1'+'cluster'+str(j)]=[group1[i][j]]

		for i in range(1):
		   for j in range(3):
		       if((group2[i][j][1][1]).strip()=='USA'):
		           dictionary_usa['group2'+'cluster'+str(j)]=[group2[i][j]]
		       else:
		           dictionary_romania['group2'+'cluster'+str(j)]=[group2[i][j]]

		for i in range(3):
		   for j in range(3):
		       if((group3[i][j][1][1]).strip()=='USA'):
		           dictionary_usa['group3'+'cluster'+str(j)]=[group3[i][j]]
		       else:
		           if((group3[i][j][1][1]).strip()=='Switzerland'):
		               dictionary_switzerland['group3'+'cluster'+str(j)]=[group3[i][j]]
		           else:
		               dictionary_romania['group3'+'cluster'+str(j)]=[group3[i][j]]


		for i in range(2):
		   for j in range(3):
		       if((group4[i][j][1][1]).strip()=='USA'):
		           dictionary_usa['group4'+'cluster'+str(j)]=[group4[i][j]]
		       else:
		           dictionary_romania['group4'+'cluster'+str(j)]=[group4[i][j]]
		dictionary_usa=str(dictionary_usa)
		dictionary_usa=dictionary_usa.replace('(','[')
		dictionary_usa=dictionary_usa.replace(')',']')
		dictionary_usa= eval(dictionary_usa)

		dictionary_romania=str(dictionary_romania)
		dictionary_romania=dictionary_romania.replace('(','[')
		dictionary_romania=dictionary_romania.replace(')',']')
		dictionary_romania= eval(dictionary_romania)

		dictionary_switzerland=str(dictionary_switzerland)
		dictionary_switzerland=dictionary_switzerland.replace('(','[')
		dictionary_switzerland=dictionary_switzerland.replace(')',']')
		dictionary_switzerland= eval(dictionary_switzerland)
		#print(group1[0][0])
		return json.dumps(dictionary_usa)
######
@app.route('/api/query_survey_results3/Switzerland', methods=['GET'])
def query_survey_results3(country_name=''):

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
		group3=x1
		#print(group3)

		country, country_result = util.country_group1()
		#print(country_result)
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
		group1=x1
		#print(group1)
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

		group2=x1
		#print(group2)
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

		group4=x1
		#print(group4)
		dictionary_usa={'country':['Unites States Of America']}
		dictionary_romania={'country':['Romania']}
		dictionary_switzerland={'country':['Switzerland']}
		for i in range(2):
		   for j in range(3):
		       if((group1[i][j][1][1]).strip()=='USA'):
		           dictionary_usa['group1'+'cluster'+str(j)]=[group1[i][j]]
		       else:
		           dictionary_romania['group1'+'cluster'+str(j)]=[group1[i][j]]

		for i in range(1):
		   for j in range(3):
		       if((group2[i][j][1][1]).strip()=='USA'):
		           dictionary_usa['group2'+'cluster'+str(j)]=[group2[i][j]]
		       else:
		           dictionary_romania['group2'+'cluster'+str(j)]=[group2[i][j]]
		print(group3)
		for i in range(3):
		   for j in range(3):

		       if((group3[i][j][1][1]).strip() =='USA'):
		           dictionary_usa['group3'+'cluster'+str(j)]=[group3[i][j]]
		       else:
		           if((group3[i][j][1][1]).strip() =='Switzerland'):

		               dictionary_switzerland['group3'+'cluster'+str(j)]=[group3[i][j]]
		           else:
		               dictionary_romania['group3'+'cluster'+str(j)]=[group3[i][j]]


		for i in range(2):
		   for j in range(3):
		       if((group4[i][j][1][1]).strip()=='USA'):
		           dictionary_usa['group4'+'cluster'+str(j)]=[group4[i][j]]
		       else:
		           dictionary_romania['group4'+'cluster'+str(j)]=[group4[i][j]]
		dictionary_usa=str(dictionary_usa)
		dictionary_usa=dictionary_usa.replace('(','[')
		dictionary_usa=dictionary_usa.replace(')',']')
		dictionary_usa= eval(dictionary_usa)

		dictionary_romania=str(dictionary_romania)
		dictionary_romania=dictionary_romania.replace('(','[')
		dictionary_romania=dictionary_romania.replace(')',']')
		dictionary_romania= eval(dictionary_romania)

		dictionary_switzerland=str(dictionary_switzerland)
		dictionary_switzerland=dictionary_switzerland.replace('(','[')
		dictionary_switzerland=dictionary_switzerland.replace(')',']')
		dictionary_switzerland= eval(dictionary_switzerland)
		#print(group1[0][0])
		print(dictionary_switzerland)
		return json.dumps(dictionary_switzerland)

@app.route('/api/query_survey_results4/Romania', methods=['GET'])
def query_survey_results4(country_name=''):

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
		group3=x1
		#print(group3)

		country, country_result = util.country_group1()
		#print(country_result)
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
		group1=x1
		#print(group1)
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

		group2=x1
		#print(group2)
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

		group4=x1
		#print(group4)
		dictionary_usa={'country':['Unites States Of America']}
		dictionary_romania={'country':['Romania']}
		dictionary_switzerland={'country':['Switzerland']}
		for i in range(2):
		   for j in range(3):
		       if(group1[i][j][1][1]=='USA'):
		           dictionary_usa['group1'+'cluster'+str(j)]=[group1[i][j]]
		       else:
		           dictionary_romania['group1'+'cluster'+str(j)]=[group1[i][j]]

		for i in range(1):
		   for j in range(3):
		       if(group2[i][j][1][1]=='USA'):
		           dictionary_usa['group2'+'cluster'+str(j)]=[group2[i][j]]
		       else:
		           dictionary_romania['group2'+'cluster'+str(j)]=[group2[i][j]]

		for i in range(3):
		   for j in range(3):
		       if(group3[i][j][1][1]=='USA'):
		           dictionary_usa['group3'+'cluster'+str(j)]=[group3[i][j]]
		       else:
		           if(group3[i][j][1][1]=='Switzerland'):
		               dictionary_switzerland['group3'+'cluster'+str(j)]=[group3[i][j]]
		           else:
		               dictionary_romania['group3'+'cluster'+str(j)]=[group3[i][j]]


		for i in range(2):
		   for j in range(3):
		       if(group4[i][j][1][1]=='USA'):
		           dictionary_usa['group4'+'cluster'+str(j)]=[group4[i][j]]
		       else:
		           dictionary_romania['group4'+'cluster'+str(j)]=[group4[i][j]]
		dictionary_usa=str(dictionary_usa)
		dictionary_usa=dictionary_usa.replace('(','[')
		dictionary_usa=dictionary_usa.replace(')',']')
		dictionary_usa= eval(dictionary_usa)

		dictionary_romania=str(dictionary_romania)
		dictionary_romania=dictionary_romania.replace('(','[')
		dictionary_romania=dictionary_romania.replace(')',']')
		dictionary_romania= eval(dictionary_romania)

		dictionary_switzerland=str(dictionary_switzerland)
		dictionary_switzerland=dictionary_switzerland.replace('(','[')
		dictionary_switzerland=dictionary_switzerland.replace(')',']')
		dictionary_switzerland= eval(dictionary_switzerland)
		#print(group1[0][0])
		return json.dumps(dictionary_romania)

if __name__ == '__main__':
	# set debug mode
	app.debug = True
	# your local machine ip
	ip = '127.0.0.1'
	app.run(host=ip)
