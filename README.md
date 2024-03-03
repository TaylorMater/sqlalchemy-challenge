Riley Taylor

UTA Data Analytics Bootcamp

Module 10 - Advanced SQL (SQL Alchemy + Flask)




## Description

This contains my submission for module 10 of the UTA Data Analytics Bootcamp. We were tasked with completing a supplied jupyter notebook to perform some analysis on the data provided, and then developing a local Flask app that would interface with the database for specific endpoints.


## Requirements

To be able to run the `app.py` or the cells in the `climate.ipynb`, you will need the following libraries:

-   sqlalchemy
-   pandas
-   matplotlib  (exclusive to `climate.ipynb`)
-   flask (exlusive to `app.py`)

The project was run using Python 3.10.13. 

## Installation

There are no binaries, the main deliverables are the jupyter notebook and the `app.py` script. Just clone this repo if you want to play with anything. You can open a jupyter notebook file in a broswer, and you can run any python script from command line or an IDE of your choice. 


## Repo Overview 

`/Resources/` contains the starter csv files and the sqlite database that the assignment revolves around.

`/SurfsUp/` contains the `app.py` script, which hosts the flask portion of the module. The name was recommended by the assignment description.

`/climate.ipynb` is the jupyter notebook that houses the analysis of the data.


## Notes

The final graph in `climate.ipynb` differs from the starter notebook graph. However, the starter notebook graph differs from the stater notebook statistics it supposedly correlates to - the mean temperature is supposed to be 71, which is true in the graph I generated, but not true in the one provided initially in the starter code. I believe the one provided in the starter code is flawed.

Also, I provided two different graphs for the inches of rain vs. date graphs near the beginning of the notebook. The first one was done over the entire dataset, no filtering or applying any functions whatsoever. This is exactly the graph that I saw in the starter notebook.

However, that graph is meaningless given the data. There are about 5-9 stations typically reporting rainfall totals for a given date, so it muddles the line plot substantially. I created an alternate graph which took the average of these datapoints, so we only had one value per date. It wasn't asked of us in the assignment, but it certainly looks cleaner. 



-----------------------------

## Sources 
### Note - many of these were used for knowledge acquisition, with no direct reference to their content in this assignment. 


Histograms — Matplotlib 3.8.3 documentation
https://matplotlib.org/stable/gallery/statistics/hist.html#sphx-glr-gallery-statistics-hist-py

Engine Configuration — SQLAlchemy 2.0 Documentation
https://docs.sqlalchemy.org/en/20/core/engines.html

Engine Configuration — SQLAlchemy 1.4 Documentation
https://docs.sqlalchemy.org/en/14/core/engines.html#sqlite

python - sqlalchemy.exc.OperationalError: (OperationalError) unable to open database file None None - Stack Overflow
https://stackoverflow.com/questions/18208492/sqlalchemy-exc-operationalerror-operationalerror-unable-to-open-database-file

python - Creating database with SQLAlchemy in Flask - Stack Overflow
https://stackoverflow.com/questions/29397002/creating-database-with-sqlalchemy-in-flask

In Python 3.5, how are triple quotes (""") considered comments by the IDE? - Stack Overflow
https://stackoverflow.com/questions/68848991/in-python-3-5-how-are-triple-quotes-considered-comments-by-the-ide

Session Basics — SQLAlchemy 2.0 Documentation
https://docs.sqlalchemy.org/en/20/orm/session_basics.html#querying

Session API — SQLAlchemy 2.0 Documentation
https://docs.sqlalchemy.org/en/20/orm/session_api.html#sqlalchemy.orm.Session.scalars

SQLAlchemy 2.0 - Major Migration Guide — SQLAlchemy 2.0 Documentation
https://docs.sqlalchemy.org/en/20/changelog/migration_20.html#migration-20-query-usage

Session Basics — SQLAlchemy 2.0 Documentation
https://docs.sqlalchemy.org/en/20/orm/session_basics.html#opening-and-closing-a-session

python - SQLAlchemy and Flask: should I use a single session for the whole API, or a session for each route? - Stack Overflow
https://stackoverflow.com/questions/76984766/sqlalchemy-and-flask-should-i-use-a-single-session-for-the-whole-api-or-a-sess

Python : What is it? Pass by Value or Pass by Reference? It is Pass by Assignment | Medium
https://medium.com/@devyjoneslocker/understanding-pythons-pass-by-assignment-in-the-backdrop-of-pass-by-value-vs-9f5cc602f943#:~:text=Python's%20behavior%20is%20neither%20purely,and%20references%20work%20in%20Python.

sql - How do I find data from this day exactly one year ago? - Stack Overflow
https://stackoverflow.com/questions/24335452/how-do-i-find-data-from-this-day-exactly-one-year-ago

datetime — Basic date and time types — Python 3.12.2 documentation
https://docs.python.org/3/library/datetime.html#timedelta-objects

Python date string to date object - Stack Overflow
https://stackoverflow.com/questions/2803852/python-date-string-to-date-object

Query API — SQLAlchemy 1.4 Documentation
https://docs.sqlalchemy.org/en/14/orm/query.html#sqlalchemy.orm.Query.filter

python - SQLAlchemy ORM conversion to pandas DataFrame - Stack Overflow
https://stackoverflow.com/questions/29525808/sqlalchemy-orm-conversion-to-pandas-dataframe

A SQLAlchemy Cheat Sheet | Codementor
https://www.codementor.io/@sheena/understanding-sqlalchemy-cheat-sheet-du107lawl

python - Group by & count function in sqlalchemy - Stack Overflow
https://stackoverflow.com/questions/1052148/group-by-count-function-in-sqlalchemy

pandas.DataFrame.sort_values — pandas 2.2.1 documentation
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html

pandas.DataFrame.plot.line — pandas 2.2.1 documentation
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.line.html

How to Rotate X-Axis Labels in a Pandas Plot
https://dataplotplus.com/how-to-rotate-x-axis-labels-in-a-pandas-plot/

How to GroupBy and Sum SQL Columns using SQLAlchemy? - GeeksforGeeks
https://www.geeksforgeeks.org/how-to-groupby-and-sum-sql-columns-using-sqlalchemy/

python - SQLAlchemy ORDER BY DESCENDING? - Stack Overflow
https://stackoverflow.com/questions/4186062/sqlalchemy-order-by-descending

Column Elements and Expressions — SQLAlchemy 1.4 Documentation
https://docs.sqlalchemy.org/en/14/core/sqlelement.html#sqlalchemy.sql.expression.desc

python - How to transfer SQL Group by results to a Pandas dataframe - Stack Overflow
https://stackoverflow.com/questions/26223721/how-to-transfer-sql-group-by-results-to-a-pandas-dataframe

Creating a Pandas dataframe using list of tuples - GeeksforGeeks
https://www.geeksforgeeks.org/creating-a-pandas-dataframe-using-list-of-tuples/

matplotlib.pyplot.plot — Matplotlib 3.8.3 documentation
https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html

How to calculate summary statistics — pandas 2.2.1 documentation
https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html

python - Get the number of rows in table using SQLAlchemy - Stack Overflow
https://stackoverflow.com/questions/10822635/get-the-number-of-rows-in-table-using-sqlalchemy

python sqlalchemy label usage - Stack Overflow
https://stackoverflow.com/questions/15555920/python-sqlalchemy-label-usage

python - Difference between filter and filter_by in SQLAlchemy - Stack Overflow
https://stackoverflow.com/questions/2128505/difference-between-filter-and-filter-by-in-sqlalchemy

python - Why use os.path.join over string concatenation? - Stack Overflow
https://stackoverflow.com/questions/13944387/why-use-os-path-join-over-string-concatenation

Why you should be using pathlib
https://treyhunner.com/2018/12/why-you-should-be-using-pathlib/

pathlib — Object-oriented filesystem paths — Python 3.12.2 documentation
https://docs.python.org/3/library/pathlib.html




