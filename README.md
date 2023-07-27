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

[1]:https://golang.dev "Golang"
[2]:https://github.com/golang-migrate/migrate "Golang Migrate"
[3]:https://github.com/mattn/go-sqlite3 "Golang SQLite3 Driver"
[4]:https://www.gnu.org/software/bash/ "GNU Bash"
[5]:https://direnv.net/ "direnv"
[6]:https://sqlite.org/index.html "SQLite3"
[7]:https://airflow.apache.org/ "Apache AirFlow"
[8]:https://www.python.org/ "Python3"
[9]:https://www.gnu.org/software/make/ "GNU Make"

## Installation Instructions
Make sure you have all the above dependencies installed.
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
4. Run your migration to create your initial db schema
```
$ make migrateup
```
5. Run the scripts in the scripts folder to fetch initial data
```
$ scripts/fetch-districts
$ scripts/fetch-categories
$ scripts/fetch-property-types
```
