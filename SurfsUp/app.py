# Import the dependencies.
from flask import Flask, jsonify

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model

# reflect the tables


# Save references to each table


# Create our session (link) from Python to the DB


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
        f"---Description: Displays all precipitation data<br/>"
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

@app.route("/api/v1.0/precipitation")
def precipitation():
    return f"Hello Rachel"

# @app.route("/api/v1.0/stations")
# def stations():
#     #code here

# @app.route("/api/v1.0/tobs")
# def tobs():
#     #code here

# @app.route("/api/v1.0/<date>")
# def one_date(date):
#     #code here

# @app.route("/api/v1.0/<startdate>/<enddate>")
# def two_date(startdate,enddate):
#     #code here








if __name__ == "__main__":
    app.run(debug=True)