HW5

## Quick Start
### Local Test Setup
First, we need to install a Python 3 virtual environment with:
```
sudo apt-get install python3-venv
```

Create a virtual environment:
```
python3 -m venv python_venv
```

You need to activate the virtual environment when you want to use it:
```
source python_venv/bin/activate
```

To fufil all the requirements for the python server, you need to run:
```
pip3 install -r requirements.txt
```
Because we are now inside a virtual environment. We do not need sudo.

### Setup local PostgresSQL Database on Windows:

* Download PostgreSQL server  www.postgresql.org .

* Once the download completes, double click on the file to run the installer.

* Click Next on the initial page to begin configuring your installation and choose your installation directory.

* The next page allows you to choose which components you wish to install. You need the PostgreSQL Server and Command Line Tools selected at a minimum.

* Click Next and choose the location where the database data files will be stored.

* select and confirm an administrative password for the PostgreSQL superuser (called postgres).

* Choose the port 5432.

* PostgreSQL is ready to be installed.

* Once the installation is complete, you can verify it using the psql command line tool.

* In your start menu, type psql and click on the tool to launch the program. You will be prompted to enter the connection details that you wish to use.

* Press Enter to accept the default choices given in the square brackets. The final prompt will be for the password for the postgres user that you configured during setup.

* PostgresSQL(pgAdmin 4) will be launched.

```

```
Create a table named covid_survey and public is the schema name for homework_webapp database.
```

CREATE TABLE public.covid_survey
(
    index integer,
    "What country do you live in?" character varying(100),
    "How old are you?" integer,
    "What is your gender?" character varying(100),
    "To what extent do you feel FEAR due to the coronavirus?" integer,
    "To what extent do you feel ANXIOUS due to the coronavirus?" integer,
    "To what extent do you feel ANGRY due to the coronavirus?" integer,
    "To what extent do you feel HAPPY due to the coronavirus?" integer,
    "To what extent do you feel SAD due to the coronavirus?" integer,
    "Which emotion is having the biggest impact on you?" character varying(1600),
    "What makes you feel that way?" character varying(1600),
    "What brings you the most meaning during the coronavirus outbrea" character varying(1600),
    "What is your occupation?" character varying(1600)
)


```
once the table is created, go to the table created on the left hand side and right click on it and select the option import/export

Select Import, provide the path of csv file under Filename option, Miscellaneous -> Header -> yes, Delimiter ->',' and then press ok and csv file data would be
imported for the table created.
```

Then you can start the server with:
```
python3 main.py
```

### Data
Survey data can be found at <mark>data/we_are_not_alone_no_nan.csv</mark>, -1 is used to represent NAN (i.e. missing data)

If your data is stored in sqlalchemy and want to output data as a python dictionary, here is [a possible solution](https://stackoverflow.com/questions/1958219/convert-sqlalchemy-row-object-to-python-dict).

### Requirements
- Create a web app including backendand and frontend to show user survey results using tables
- Choose any database (such as PostgreSQL and sqlalchemy) you like to store [user survey data](data/we_are_not_alone_no_nan.csv).
- Retrieve user suvey data from your database and split data into groups
	- Step 1, split data based on age and gender
		- Group 1: young (<=35) male
		- Group 2: middle-aged or old (>=36) male
		- Group 3: young (<=35) female
		- Group 2: middle-aged or old (>=36) female
	- Step 2, split data groups generated from Step 1 into based smaller groups based on countries, such as US groups and Canada groups.
	- Step 3, check which groups from Step 2 have more than 10 elements. If yes, use KMeans (check util.cluster_user_data and util.split_user_data) to split them into subgroups.
- Visualize all the groups with tables on the frontend (check sample code in hw5)


