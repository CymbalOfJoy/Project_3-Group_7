from sqlalchemy import create_engine, text
import pandas as pd
import numpy as np
# Plotting
import matplotlib.pyplot as plt
import seaborn as sns

import os


class SQLHelper:

    def __init__(self):
        os.chdir(os.path.dirname(os.path.realpath(__file__)))       
        self.engine = create_engine("sqlite:///touristtravel.sqlite")

    # Query 1 for line chart - sorting table by the column Total_Travel_Cost To be displayed on Dashboard page
    def query_line_data(self):
        conn = self.engine.connect()  # Raw SQL/Pandas
        query = text("""SELECT
                   Main_Purpose,
                   SUM(Total_Travel_Cost) AS Total_Cost
                FROM
                    touristtravel
                GROUP BY
                   Main_Purpose
                ORDER BY
                   Total_Cost ASC;""")
        df = pd.read_sql(query, con=conn)
        print(df)
        conn.close()
        return df
    
    # Query 2 Creating the data Table to display on Dashboard page 
    ## INSTERT TABLE ONCE COMPLETED STILL WORKING -BM 02/15/2025
    def query_table_data(self):
        conn = self.engine.connect()  # Raw SQL/Pandas
        query = text("""SELECT
                  *
                FROM
                    touristtravel
                        """)
        df = pd.read_sql(query, con=conn)
        print(df)
        conn.close()
        return df

    # Query 3 for bar chart - pulling data from table, sorting by the accommodation type
    ## COMPLETE, NEED TO WORK INTO DASHBOARD/app.JS page 
    def query_bar_data(self):
        conn = self.engine.connect()  # Raw SQL/Pandas
        query = text ("""SELECT
                   Main_Purpose,
                   SUM(Total_Travel_Cost) AS Total_Cost
                FROM
                    touristtravel
                GROUP BY
                   Main_Purpose
                ORDER BY
                   Total_Cost ASC;""")
        df = pd.read_sql(query, con=conn)
        conn.close()
        return df
    
        # Query 4 for Bubble Chart (-Travel Cost in comparrison to Accomidation )
    ## COMPLETE, NEED TO WORK INTO DASHBOARD/app.JS page 
    def query_bar_data(self):
        conn = self.engine.connect()  # Raw SQL/Pandas
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
        df1 = pd.read_sql(query, con=conn)
        # Plotting the bar chart
        # Plotting the bar chart
        plt.figure(figsize=(10, 6))
        plt.bar(df1['Main_Purpose'], df1['Total_Cost'], color=['firebrick', 'royalblue', 'limegreen'])
        plt.title("Comparison of Total Travel Cost by Main Purpose")
        plt.xlabel("Main Purpose")
        plt.ylabel("Total Travel Cost")

        # Setting the y-axis limit before applying currency formatting
        plt.ylim(800000, df1['Total_Cost'].max() * 1.1)  # Setting the y-axis limit

        # Formatting the y-axis to show currency format
        plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${x:,.2f}"))
        plt.grid(True)
        plt.tight_layout()  # Adjust the layout to ensure everything fits without overlapping
        plt.show()
        # Save the plot as an image file
        plt.savefig('static/images/travel_cost_chart.png')
        plt.close()

        conn.close()
        return df1

    # Query 5 for pie/donut chart - pulling data from table, sorting by the column Reason_for_Travel(INCOMPLETE)
    def query_pie_data(self):
        conn = self.engine.connect()  # Raw SQL/Pandas
        query = text("""SELECT *
                        FROM touristtravel
                        ORDER BY Reason_for_Travel""")
        df = pd.read_sql(query, con=conn)
        conn.close()
        return
    
        # Query 6 for Map Data (INCOMPLETE)
    def query_map_data(self):
        conn = self.engine.connect()  # Raw SQL/Pandas
        query = text("""SELECT *
                        FROM touristtravel
                        """)
        df = pd.read_sql(query, con=conn)
        conn.close()
        return