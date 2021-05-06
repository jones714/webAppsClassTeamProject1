from sklearn.cluster import KMeans
from flask import Flask, render_template
import numpy as np
import psycopg2
import time


def cluster_user_data(result, emotional_col_start=4, emotional_col_end=9, n_clusters=3):
	'''
	This function cluster user data based on KMeans algorithm
	By default, it will split your data into three groups
	'''
	# collect answers for five emotional questions
	# which are located from 4th col to 9th col

	emotional_data = [i[emotional_col_start:emotional_col_end] for i in result]

	# use kmeans to cluster data
	kmeans = KMeans(n_clusters).fit(emotional_data)
	# return cluster labels
	return kmeans.labels_

def split_user_data(result, labels, n_clusters=3):
	'''
	this function will split input data into groups
	based on labels
	'''
	result_list = []
	for i in range(n_clusters):
		# find indices of each group elements, without [0] the result is tuple
		tmp_indices = np.where(labels == i)[0]
		result_list.append([result[i] for i in tmp_indices])

	return result_list

def group1():
	try:
	    conn = psycopg2.connect(database="homework_webapp", user="postgres",
	    password="******", host="localhost")
	    print("connected")
	except:
	    print ("I am unable to connect to the database")
	mcursor =conn.cursor()

	mcursor.execute("""SELECT * FROM public.covid_survey where "How old are you?" <= 35 and "What is your gender?" ='Male'; """)
	result = mcursor.fetchall()
	return result

def group2():
	try:
	    conn = psycopg2.connect(database="homework_webapp", user="postgres",
	    password="******", host="localhost")
	    print("connected")
	except:
	    print ("I am unable to connect to the database")
	mcursor =conn.cursor()

	mcursor.execute("""SELECT * FROM public.covid_survey where "How old are you?" >= 36 and "What is your gender?" ='Male'; """)
	result = mcursor.fetchall()
	return result

def group3():
	try:
	    conn = psycopg2.connect(database="homework_webapp", user="postgres",
	    password="******", host="localhost")
	    print("connected")
	except:
	    print ("I am unable to connect to the database")
	mcursor =conn.cursor()

	mcursor.execute("""SELECT * FROM public.covid_survey where "How old are you?" <= 35 and "What is your gender?" ='Female'; """)
	result = mcursor.fetchall()
	return result

def group4():
	try:
	    conn = psycopg2.connect(database="homework_webapp", user="postgres",
	    password="******", host="localhost")
	    print("connected")
	except:
	    print ("I am unable to connect to the database")
	mcursor =conn.cursor()

	mcursor.execute("""SELECT * FROM public.covid_survey where "How old are you?" >= 36 and "What is your gender?" ='Female'; """)
	result = mcursor.fetchall()
	return result

def allcountry():
	try:
	    conn = psycopg2.connect(database="homework_webapp", user="postgres",
	    password="******", host="localhost")
	    print("connected")
	except:
	    print ("I am unable to connect to the database")
	mcursor =conn.cursor()

	#Create a list all_countires containing elements as list f group1,2,3,4

	group_1=group1()

	group_2=group2()
	group_3=group3()
	group_4=group4()
	countrydict1={}
	countrydict2={}
	countrydict3={}
	countrydict4={}
	for i in group_1:
		if i[1] not in countrydict1:
			countrydict1[i[1]]=[i]
		else:
			countrydict1[i[1]].append(i)

	for i in group_2:
		if i[1] not in countrydict2:
			countrydict2[i[1]]=[i]
		else:
			countrydict2[i[1]].append(i)


	for i in group_3:
		if i[1] not in countrydict3:
			countrydict3[i[1]]=[i]
		else:
			countrydict3[i[1]].append(i)

	for i in group_4:
		if i[1] not in countrydict4:
			countrydict4[i[1]]=[i]
		else:
			countrydict4[i[1]].append(i)

	print("countrydict1")
	print(countrydict1.values())

	time.sleep(5)
	print("countrydict2")
	print(countrydict2)
	time.sleep(5)
	print("countrydict3")
	print(countrydict3)
	time.sleep(5)
	print("countrydict4")
	print(countrydict4)
	#for item in result:

	return result

def country_group1():
	#get list of countries for group1
	try:
	    conn = psycopg2.connect(database="homework_webapp", user="postgres",
	    password="******", host="localhost")
	    print("connected")
	except:
	    print ("I am unable to connect to the database")
	mcursor =conn.cursor()
	#get list of countries for group1 SQL is as per group 1
	mcursor.execute("""SELECT distinct("What country do you live in?") FROM public.covid_survey where "How old are you?" <= 35 and "What is your gender?" ='Male';""")
	result_country = mcursor.fetchall()
	#here we remove duplicate names of countries that we got from previous step
	result=list(set([i[0].strip() for i in result_country]))
	#result=['Israel', 'UK', 'Romania', 'USA', 'Switzerland', 'Rwanda', 'Canada', 'Ireland l', 'Germany']
	#initializing a dictionary that would contain all the data pertaining to a particular country
	dict_country_group1={}
	for country in result:
		# Fetch all rows for first country (each item from result)
		sqldata=str("""SELECT * FROM public.covid_survey where "How old are you?" <= 35 and "What is your gender?" ='Male' and "What country do you live in?" like '{}%'; """).format(country)
		mcursor.execute(sqldata)
		country_data=mcursor.fetchall()
		#this creates a dictionary for example USA with a list of rows
		dict_country_group1[country]=country_data


	#print(dict_country_group1)
	return result, dict_country_group1
	# iterate through list and get tables for each country based on eah group
	#feed the tables to both functions

def country_group2():
	#get list of countries for group1
	try:
	    conn = psycopg2.connect(database="homework_webapp", user="postgres",
	    password="******", host="localhost")
	    print("connected")
	except:
	    print ("I am unable to connect to the database")
	mcursor =conn.cursor()
	#get list of countries for group1 SQL is as per group 1
	mcursor.execute("""SELECT distinct("What country do you live in?") FROM public.covid_survey where "How old are you?" >= 36 and "What is your gender?" ='Male';""")
	result_country = mcursor.fetchall()
	#here we remove duplicate names of countries that we got from previous step
	result=list(set([i[0].strip() for i in result_country]))
	#result=['Israel', 'UK', 'Romania', 'USA', 'Switzerland', 'Rwanda', 'Canada', 'Ireland l', 'Germany']
	#initializing a dictionary that would contain all the data pertaining to a particular country
	dict_country_group2={}
	for country in result:
		# Fetch all rows for first country (each item from result)
		sqldata=str("""SELECT * FROM public.covid_survey where "How old are you?" >= 36 and "What is your gender?" ='Male' and "What country do you live in?" like '{}%'; """).format(country)
		mcursor.execute(sqldata)
		country_data=mcursor.fetchall()
		#this creates a dictionary for example USA with a list of rows
		dict_country_group2[country]=country_data


	#print(dict_country_group1)
	return result, dict_country_group2
	# iterate through list and get tables for each country based on eah group
	#feed the tables to both functions


def country_group3():
	#get list of countries for group1
	try:
	    conn = psycopg2.connect(database="homework_webapp", user="postgres",
	    password="******", host="localhost")
	    print("connected")
	except:
	    print ("I am unable to connect to the database")
	mcursor =conn.cursor()
	#get list of countries for group1 SQL is as per group 1
	mcursor.execute("""SELECT distinct("What country do you live in?") FROM public.covid_survey where "How old are you?" <= 35 and "What is your gender?" ='Female';""")
	result_country = mcursor.fetchall()
	#here we remove duplicate names of countries that we got from previous step
	result=list(set([i[0].strip() for i in result_country]))
	#result=['Israel', 'UK', 'Romania', 'USA', 'Switzerland', 'Rwanda', 'Canada', 'Ireland l', 'Germany']
	#initializing a dictionary that would contain all the data pertaining to a particular country
	dict_country_group3={}
	for country in result:
		# Fetch all rows for first country (each item from result)
		sqldata=str("""SELECT * FROM public.covid_survey where "How old are you?" <= 35 and "What is your gender?" ='Female' and "What country do you live in?" like '{}%'; """).format(country)
		mcursor.execute(sqldata)
		country_data=mcursor.fetchall()
		#this creates a dictionary for example USA with a list of rows
		dict_country_group3[country]=country_data


	#print(dict_country_group1)
	return result, dict_country_group3
	# iterate through list and get tables for each country based on eah group
	#feed the tables to both functions


def country_group4():
	#get list of countries for group1
	try:
		conn = psycopg2.connect(database="homework_webapp", user="postgres",
		password="******", host="localhost")
		print("connected")
	except:
		print ("I am unable to connect to the database")
	mcursor =conn.cursor()
	#get list of countries for group1 SQL is as per group 1
	mcursor.execute("""SELECT distinct("What country do you live in?") FROM public.covid_survey where "How old are you?" >= 36 and "What is your gender?" ='Female';""")
	result_country = mcursor.fetchall()
	#here we remove duplicate names of countries that we got from previous step
	result=list(set([i[0].strip() for i in result_country]))
	#result=['Israel', 'UK', 'Romania', 'USA', 'Switzerland', 'Rwanda', 'Canada', 'Ireland l', 'Germany']
	#initializing a dictionary that would contain all the data pertaining to a particular country
	dict_country_group4={}
	for country in result:
		# Fetch all rows for first country (each item from result)
		sqldata=str("""SELECT * FROM public.covid_survey where "How old are you?" >= 36 and "What is your gender?" ='Female' and "What country do you live in?" like '{}%'; """).format(country)
		mcursor.execute(sqldata)
		country_data=mcursor.fetchall()
		#this creates a dictionary for example USA with a list of rows
		dict_country_group4[country]=country_data


	#print(dict_country_group1)
	return result, dict_country_group4
	# iterate through list and get tables for each country based on eah group
	#feed the tables to both functions
# new code here

def mapcountry(j):
	if j=='USA' or j=='Usa':
		j='United States of America'
	if j=='UK':
		j='United Kingdom'
	if j=='spain':
		j='Spain'
	if j=='Ireland l':
		j='Ireland'
	return j

def allcountryy():
	try:
		conn = psycopg2.connect(database="homework_webapp", user="postgres",
		password="******", host="localhost")
		print("connected")
	except:
		print ("I am unable to connect to the database")
	mcursor =conn.cursor()
		#get list of countries for group1 SQL is as per group 1
	mcursor.execute("""SELECT distinct("What country do you live in?") FROM public.covid_survey;""")
	result_country = mcursor.fetchall()
	result=list(set([i[0].strip() for i in result_country]))
	result_final=list(map(mapcountry, result))
	return result_final
