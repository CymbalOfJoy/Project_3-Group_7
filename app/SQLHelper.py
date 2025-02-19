from sqlalchemy import create_engine, text
import pandas as pd
import numpy as np
# Plotting
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

import os


class SQLHelper:

    def __init__(self):
        os.chdir(os.path.dirname(os.path.realpath(__file__)))       
        self.engine = create_engine("sqlite:///touristtravel.sqlite")


    def query_bar_data(self):
        conn = self.engine.connect()
        query = text("""SELECT
                   Main_Purpose,
                   SUM(Total_Travel_Cost) AS Total_Cost
                FROM
                    touristtravel
                GROUP BY
                   Main_Purpose
                ORDER BY
                   Total_Cost ASC;""")
       
        df1 = pd.read_sql(query, con=conn)
        return df1

    def query_bubble_data(self):
        conn = self.engine.connect()
        query = text("""
            SELECT
                Mode_of_Travel,
                Main_Purpose,
                COUNT(*) AS Travel_Count
            FROM
                touristtravel
            GROUP BY
                Mode_of_Travel,
                Main_Purpose
            ORDER BY
                Main_Purpose;
        """)
        df2 = pd.read_sql(query, con=conn)

        df2_sorted = df2.sort_values(by='Travel_Count', ascending=False)
        return df2_sorted
    
    def query_table_data(self, Country_Visited=None):
        conn= self.engine.connect() 
        query = """
            SELECT
                City_Visited,
                Country_Visited,
                Travel_Duration_Days,
                Number_of_Companions,
                Accommodation_Type,
                Main_Purpose,
                Season_of_Visit
            FROM
                touristtravel
        """
        if Country_Visited:
            query += " WHERE Country_Visited = :Country_Visited"
        query += " ORDER BY Country_Visited;"
        df3 = pd.read_sql(query, con=conn, params={"Country_Visited": Country_Visited})

        return df3

    def pie_data(self):
        conn = self.engine.connect()
        query = text("""
        SELECT
            City_Visited,
            Country_Visited,
            Travel_Duration_Days,
            Number_of_Companions,
            Accommodation_Type,
            Main_Purpose,
            Season_of_Visit
        FROM
            touristtravel
        ORDER BY
            Country_Visited;
        """)
        df3 = pd.read_sql(query, con=conn)
        return df3
    
    def query_map_data(self):
        conn = self.engine.connect()
        query = text("""
        SELECT City_Visited, lat, long, MIN(Country_Visited) as min_cv, SUM(Number_of_Companions) as sum_nc
        FROM touristtravel         
        GROUP BY City_Visited         
        """)
        df3 = pd.read_sql(query, con=conn)
        return df3