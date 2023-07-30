# Quant DealApp AirFlow
The Quant Airflow project for scheduled collection of dealapp.sa property
listings.

## Dependencies
* [Bash][4] >= 5.0
* [Make][9]
* [direnv][5]
* [Golang][1] >= 1.18
* [golang-migrate][2]
* [go-sqlite3][3]
* [SQLite3][6]
* [AirFlow][7]
* [Python][8] > 3.0
* [JQ][10]

## Installation Instructions
Following are instructions to how to get the solution up and running.
* Note: Make sure you have all the above dependencies installed.
1. Clone the repository into your local drive by running the following:
```
$ git clone https://github.com/moeabdol/quant-airflow.git
```
2. Create and activate a python virtual environment
```
$ cd quant-airflow
$ python3 -m venv .venv
$ source .venv/bin/activate
```
3. Install your python dependencies
```
$ pip install -r requirements.txt
```
4. Run your migrations to create the initial db schema
```
$ make migrateup
```
5. Run the scripts in the scripts folder to fetch initial data
```
$ scripts/fetch-districts
$ scripts/fetch-categories
$ scripts/fetch-property-types
```
6. Run AirFlow standalone instance
```
$ airflow standalone
```
7. Finally from within AirFlow UI, activate the DAG labeled
`fetch_listings_dag_v3` and the DAG will run daily mid-night `Asia/Riyadh` time.

## Database Schema & Migrations
For creating and maintaining migrations we use `golang-migrate`. It is an
effective and  widely used migration tool. All migrations up/down exist under
the `migrations` directory. All migrations run against the sqlite3 `dealapp.db`.
Following are the tables in this database.
* `cities` - Table to hold city data
* `districts` - Table to hold city district data
* `categories` - Table to hold property category data
* `property_types` - Table to hold property type data
* `property_listings` - Table to hold advertised property listings data

## Fetch Scripts
For collecting the initial district and category related data we use 3
bash scripts to call the respective REST endpoints and populate the database
with the initial data we are going to use later to get property listings.
Following are the scripts:
1. `scripts/fetch-districts` - Bash script to fetch all city districts
2. `scripts/fetch-categories` - Bash script to fetch all property categories
3. `scripts/fetch-property-types` - Bash script to fetch all property types
* Note: that for the initial city data, we collected the ids of the 12 advertised
cities manually and included them in the initial city table migration as INSERT
statements.

## Fetch Property Listing AirFlow DAG
The `fetch_listings_dag_v3` is a simple AirFlow DAG to handle all tasks related
to fetching city-specific data. It contains 2 main task types
1. `SqliteOperator` task to make sure the database is cleaned before fetching of
   data
2. `PythonOperator` task(s) one per each city to fetch city related listings

### Task Dependency
Before the actual fetching of data the `SqliteOperator` task
`clear_property_listings_table_task` is run to ensure no conflicting primary key
constraints exist, or duplicated data. Once that is done, all `PythonOperator`
tasks relating to each city run in parallel.
![][task_graph]
* Note: Since this is running in a development environment, the
SequentialExecutor is used; hence, all tasks will run sequentially as opposed to
a run in production using a LocalExecutor or CeleryExecutor where all tasks
should run in-parallel.

## Fetch City Listings Task
The code for this task is in `dags/fetch_city_listings.py`. I have separated the
code for modularity, isolation and ease of testing. This is a simple python
script that takes as input the `name_en` for a city and then query the database
for all districts in that city and fetch all property listings pages (10
listings per request).

## Assumptions
* This is a development system and uses sqlite backend
* This is a development system and uses a SequentialExecutor

[1]:https://golang.dev "Golang"
[2]:https://github.com/golang-migrate/migrate "Golang Migrate"
[3]:https://github.com/mattn/go-sqlite3 "Golang SQLite3 Driver"
[4]:https://www.gnu.org/software/bash/ "GNU Bash"
[5]:https://direnv.net/ "direnv"
[6]:https://sqlite.org/index.html "SQLite3"
[7]:https://airflow.apache.org/ "Apache AirFlow"
[8]:https://www.python.org/ "Python3"
[9]:https://www.gnu.org/software/make/ "GNU Make"
[10]:https://github.com/jqlang/jq "Command-line JSON Parser"

[task_graph]:images/2023-07-30_01-28.png "Task Graph"
