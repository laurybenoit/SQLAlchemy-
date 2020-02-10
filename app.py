# Import Flask
from flask import Flask, jsonify
import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy.pool import StaticPool

# reflect an existing database into a new model
Base = automap_base()
#Database set up
engine= create_engine("sqlite:///hawaii.sqlite")
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Passenger = Base.classes.passenger
Station = Base.classes.station
session = Session(engine)

# flask set up
app = Flask(__name__)

#Flask Routes
@app.route("/")
def Homepage():
    """List all available api routes"""
    return (
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>"
    )



