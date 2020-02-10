# Import Flask
from flask import Flask, jsonify
import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import func
from sqlalchemy.pool import StaticPool

# reflect an existing database into a new model
Base = automap_base()
#Database set up
engine= create_engine("sqlite:///hawaii.sqlite", echo=False)
# reflect the tables
Base.prepare(engine, reflect=True)
Base.classes.keys()

# Save reference to the table
Precipitation = Base.classes.precipitation
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
#precipitation
@app.route("/api/v1.0/precipitation")
def precipitation():
    previous_year = dt.date(2017,8,23) - dt.timedelta(days=365)
    prcp_data = session.query(Measurement.date, Measurement.prcp).\
                filter(Measurement.date >= previous_year).\
                order_by(Measurement.date).all()
    prcp_list = dict(prcp_data)
    return jsonify(prcp_list)

@app.route("/api/v1.0/stations")
def stations():
    all_stations = session.query(Station.station, Station.name).all()
    station_list = list(all_stations)
    return jsonify(station_list)

@app.route("/api/v1.0/tobs")
def tobs():
    previous_year_tobs = dt.date(2017,8,23) - dt.timedelta(days=365)
    tobs_date = session.query(Measurement.date, Measurement.prcp).\
                filter(Measurement.date >= previous_year).\
                order_by(Measurement.date).all()
    tobs_list = list(tobs_date)
    return jsonify(tobs_list)

@app.route("/api/v1.0/<start>")
def start():
    start_day = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                filter(Measurement.date >= start).\
                group_by(Measurement.date).all()
    start_list = list(start_day)
    return jsonify(start_list)

@app.route("/api/v1.0/<start>/<end>")
def start_end():
    start_end = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                filter(Measurement.date >= start).\
                filter(Measurement.date <= end).\
                group_by(Measurement.date).all()
    start_end_list = list(start_end)
    return jsonify(start_end_list)

    if __name__ == '__main__':
        app.run(debug=True)

