import pandas as pd
from flask import Flask, jsonify, render_template, redirect, request
from SQLHelper import SQLHelper

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0  # remove caching

# SQL Helper
sql_helper = SQLHelper()

#################################################
# Flask STATIC Routes
#################################################

@app.route("/")
def welcome():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/map")
def map():
    return render_template("map.html")

@app.route("/about_us")
def about_us():
    return render_template("about_us.html")

@app.route("/works_cited")
def works_cited():
    return render_template("works_cited.html")

#################################################
# API Routes
#################################################

@app.route("/api/v1.0/bubbledata/")
def bubbledata():
    # Execute queries
    df2 = sql_helper.query_bubble_data()
    # Turn DataFrame into List of Dictionary
    data = df2.to_dict(orient="records")
    return jsonify(data)

@app.route("/api/v1.0/bar_data/")
def bar_data():
    # Execute Query
    df1 = sql_helper.query_bar_data()
    # Turn DataFrame into List of Dictionary
    data = df1.to_dict(orient="records")
    return jsonify(data)

@app.route("/api/v1.0/table_data/<Country_Visited>")
def filter_data(Country_Visited):
    df = sql_helper.query_table_data(Country_Visited)
    data = df.to_dict(orient="records")
    return jsonify(data)

@app.route("/api/v1.0/pie_data/")
def pie_data():
    # Execute Query
    df = sql_helper.query_pie_data()
    # Turn DataFrame into List of Dictionary
    data = df.to_dict(orient="records")
    
    # # Create a pie chart for the 'Country_Visited' column
    # plt.figure(figsize=(10, 7))
    # df.set_index('Country_Visited')['Count'].plot.pie(autopct='%1.1f%%', startangle=140, cmap='viridis')
    # plt.title('Precentage of Visitors to Each Country')
    # plt.ylabel('')  # This removes the y-label
    # plt.savefig('static/pie_chart.png')
    # plt.tight_layout()
    # plt.show()  

    # Return the JSON data
    return jsonify(data) 

@app.route("/api/v1.0/map_data/")
def map_data():
    # Execute Query
    df = sql_helper.query_map_data()
    # Turn DataFrame into List of Dictionary
    data = df.to_dict(orient="records")
    return jsonify(data)

#################################################
# ELIMINATE CACHING
#################################################

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

if __name__ == "__main__":
    print("starting app")
    app.run(debug=True)
