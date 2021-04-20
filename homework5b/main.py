import json

from flask import Flask, render_template
import util
import psycopg2

app = Flask(__name__)


@app.route('/')
def WelcomePage():
    return render_template('WelcomePage.html')

@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/surveyCountry', methods=['GET'])
def allCountry():
    result = util.surveyResult()
    print(result)
    return result


@app.route('/group1', methods=['GET'])
def test():
    result = util.group1()
    return json.dumps(result)


@app.route('/group2')
def test2():
    result = util.group2()
    labels = util.cluster_user_data(result)
    return result


@app.route('/group3')
def test3():
    result = util.group3()
    labels = util.cluster_user_data(result)
    return result


@app.route('/group4')
def test4():
    result = util.group4()
    labels = util.cluster_user_data(result)
    return result


@app.route('/country_group1')
def test6():
    country, country_result = util.country_group1()
    for country_item in country:
        if len(country_result[country_item]) > 10:
            result = util.group1()
            labels = util.cluster_user_data(result)
            result1 = util.split_user_data(country_result[country_item], labels)
            return result1
        else:
            result = util.group1()
            labels = util.cluster_user_data(result)
            return result


if __name__ == '__main__':
    # set debug mode
    app.debug = True
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)
