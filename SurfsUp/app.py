# Import the dependencies.
from flask import Flask, jsonify

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import numpy as np
import pandas as pd
import datetime as dt


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station



#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################

# index route
@app.route("/")
def home():
    #print request recieved to terminal
    print(f"Server recieved request for index route")

    #return all avaliable routes to app
    return (
        f"Welcome to Hawaii Climate API! <br/>"
        f"Available Routes:<br/>"
        '<br/>'
        f"/api/v1.0/precipitation<br/>"
        f"---Description: Displays all precipitation data from 2017-08-23 to 2018-08-23<br/>"
        '<br/>'
        f"/api/v1.0/stations<br/>"
        f"---Description: Displays list of all Stations <br/>"
        '<br/>'
        f"/api/v1.0/tobs<br/>"
        f"---Description: Displays dates and temperature observations from most active station for the previous year<br/>"
        '<br/>'
        f"/api/v1.0/YYYY-MM-DD<br/>"
        f"---Description: Displays min, max, and avg temperatures for start date (date required as end arguement)<br/>"
        '<br/>'
        f"/api/v1.0/YYYY-MM-DD/YYYY-MM-DD<br/>"
        f"---Description: Displays min, mac, and avg temperatures from start date to end date (start date and end date required as end arguement) <br/>"
    )

#create route that return most recent 12 months of precip data
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    #get most recent date
    recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    # Design a query to retrieve the last 12 months of precipitation data
    # Starting from the most recent data point in the database. 
    recent_date_as_date = dt.datetime.strptime(recent_date[0],'%Y-%m-%d').date()

    # Calculate the date one year from the last date in data set.
    one_year = recent_date_as_date - dt.timedelta(days=365)
    one_year_string = one_year.strftime('%Y-%m-%d')

    # Perform a query to retrieve the data and precipitation scores
    prcp_results = session.query(Measurement.date, Measurement.prcp).\
                filter(Measurement.date <=recent_date[0]).\
                filter(Measurement.date >=one_year_string).all()

    session.close()

    #create empty list to store data
    prcp_list = []
    for date, prcp in prcp_results:
        prcp_dict = {date:prcp}
        prcp_list.append(prcp_dict)

    return jsonify(prcp_list)

#create route to return a list of all stations
@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    #make query to get list of all stations
    stations = session.query(Measurement.station, Station.name).\
                        filter(Measurement.station == Station.station).\
                        group_by(Measurement.station).all()
    session.close()
    
    station_list = []
    for station, name in stations:
        station_dict = {}
        station_dict['Station_ID'] = station
        station_dict['Station Name'] = name

        station_list.append(station_dict)

    return jsonify(station_list)



# @app.route("/api/v1.0/tobs")
# def tobs():
#     return f""

# @app.route("/api/v1.0/<date>")
# def one_date(date):
#     return f""

# @app.route("/api/v1.0/<startdate>/<enddate>")
# def two_date(startdate,enddate):
#     return f""








if __name__ == "__main__":
    app.run(debug=True)