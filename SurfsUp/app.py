# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

from pathlib import Path
import datetime as dt

#################################################
# Database Setup
#################################################
# Get the current script's directory
script_dir = Path(__file__).resolve().parent

# Define the relative path to the database
db_relative_path = script_dir / '..' / 'Resources' / 'hawaii.sqlite'
#had to do the above because the relative paths I provided didn't resolve properly, the current working directory I guess was different than "SurfsUp, but strangely it also failed when I assumed the current working directory was the sqlalchemy-challenge directory. 

#best practice is to avoid worrying about it by computing the absolute path whenever we need to connect


engine = create_engine(f"sqlite:///{db_relative_path}")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Stations = Base.classes.station
Measurements = Base.classes.measurement

# Create our session (link) from Python to the DB
#INSTEAD OF ONE GLOBAL SESSION, A NEW SESSION WILL BE CREATED AT EVERY ROUTE REQUEST, see route implementation below


#################################################
# Util Functions
#################################################
def get_last_year(session):
    #returns the most recent observed date in the data set, minus 365 days, as a datetime object
    # I wonder if we close the session here, would we break the session dependent code in the function that called this one?
    recent_date = session.query(func.max(Measurements.date)).first()
    # Calculate the date one year from the last date in data set.
    one_year_delta = dt.timedelta(days=365)
    last_year_date = dt.date.fromisoformat(recent_date[0]) - one_year_delta
    return(last_year_date)
####



def get_most_frequent_station(session):
    #returns the string for the name of the station that has the most entries in the measurements table
    station_counts = (
        session
        .query(Measurements.station, func.count(Measurements.station).label('count'))
        .group_by(Measurements.station)
        .order_by(sqlalchemy.desc('count'))
        .all()
    )
    return(station_counts[0][0])
####



def query_reults_to_list(results):
    #returns a list of dicts, where each dict is a row from a query
    #only applicable to queries that selected all columns from a table
    entries = []

    #we need to determine what mapped class we referenced in our query:
    mapped_class = results[0].__class__
    
    for entry in results:
        entry_dict = {}
        #neat way to use the results from a query to dynamically create dicts for each row

        for col in mapped_class.__table__.columns.keys():
            entry_dict[col] = getattr(entry, col)
        entries.append(entry_dict)

    return(entries)
####




#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    
    #python uses implicit string concatenation, so the code below is essentially just returning a single string with line breaks
    return (
        "/api/v1.0/precipitation<br/>"
        "/api/v1.0/stations<br/>"
        "/api/v1.0/tobs<br/>"
        "<br/>"
        "For the start and end dates for the routes below, be sure to have dates in ISO date format: YYYY-MM-DD<br/>"
        "<br/>"
        "/api/v1.0/tstats/&ltstart&gt<br/>"
        "/api/v1.0/tstats/&ltstart&gt/&ltend&gt<br/>"

    )




@app.route("/api/v1.0/precipitation")
def precipitation():
    # Returns json with the date as the key and the value as the precipitation. Only returns the jsonified precipitation data for the last year in the database

    #set up a session for the request
    session = Session(engine)
    #find most recent date
    last_year_date = get_last_year(session)

    query_reults = (
        session
        .query(Measurements.date, Measurements.prcp)
        .filter(Measurements.date > last_year_date)
        .order_by(Measurements.date)
        .all()
        )

    #close the session
    session.close()

    #we only want date and prcp
    precipitation_entries = []
    for date, prcp in query_reults:
        weather_entry_dict = {}
        weather_entry_dict['date'] = date
        weather_entry_dict['prcp'] = prcp
        precipitation_entries.append(weather_entry_dict)

    return (
        jsonify(precipitation_entries)
    )




@app.route("/api/v1.0/stations")
def stations():
    # Returns jsonified data of all of the stations in the database
    
    #create session for request
    session = Session(engine)
    query_results = (
        session
        .query(Stations)
        .all()
    )

    #close session for request
    session.close()

    station_entries = query_reults_to_list(query_results)
    return (
        jsonify(station_entries)
    )




@app.route("/api/v1.0/tobs")
def tobs():
    # Returns jsonified data for the most active station (USC00519281) 
    # Only returns the jsonified data for the last year of data
    
    #create session for request
    session = Session(engine)
    
    #we need to find the limits of our filters
    last_year_date = get_last_year(session)
    desired_station = get_most_frequent_station(session)

    query_results = (
        session
        .query(Measurements)
        .filter(Measurements.date > last_year_date)
        .filter(Measurements.station == desired_station)
        .order_by(Measurements.date)
        .all()
    )

    #close session for request
    session.close()
    
    tobs_entries = query_reults_to_list(query_results)
    return (
        jsonify(tobs_entries)
    )


@app.route("/api/v1.0/tstats/<start>")
def start(start):
# Accepts the start date as a parameter from the URL
# Returns the min, max, and average temperatures calculated from the given start date to the end of the dataset


#start date is expected to be in ISO format, i.e. a string that looks like YYYY-MM-DD
#surprisingly, if we used Python 3.11 isntead of Python 3.10, we could get YYYYMMDD ISO dates

    start_date = dt.date.fromisoformat(start)
    session = Session(engine)
    query_results = (
        session
        .query(func.min(Measurements.tobs).label('Min'), 
               func.max(Measurements.tobs).label('Max'),
               func.avg(Measurements.tobs).label('Avg'))
        .filter(Measurements.date > start_date)
        .all()
    )

    stat_dict = {}
    #query results are a list of tuples, with only one tuple, which has 3 values
    #this is essentially saying, for every tuple in this list, we want to assign them in order to these variable names and then do the normal for loop
    for min, max, avg in query_results:
        stat_dict['min'] = min
        stat_dict['max'] = max
        stat_dict['avg'] = avg
    return jsonify(stat_dict)





@app.route("/api/v1.0/tstats/<start>/<end>")
def start_end(start, end):
# Accepts the start date as a parameter from the URL
# Returns the min, max, and average temperatures calculated from the given start date to the given end date.

#start/end date is expected to be in ISO format, i.e. a string that looks like YYYY-MM-DD
    start_date = dt.date.fromisoformat(start)
    end_date = dt.date.fromisoformat(end)
    session = Session(engine)
    query_results = (
        session
        .query(func.min(Measurements.tobs).label('Min'), 
               func.max(Measurements.tobs).label('Max'),
               func.avg(Measurements.tobs).label('Avg'))
        .filter(Measurements.date > start_date)
        .filter(Measurements.date < end_date)
        .all()
    )

    stat_dict = {}
    #query results are a list of tuples, with only one tuple, which has 3 values
    for min, max, avg in query_results:
        stat_dict['min'] = min
        stat_dict['max'] = max
        stat_dict['avg'] = avg
    return jsonify(stat_dict)




if __name__ == '__main__':
    app.run(debug=True)
