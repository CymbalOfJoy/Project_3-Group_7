from sqlalchemy import create_engine, text
import pandas as pd
import numpy as np
# Plotting
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly as plt

import json
import os


class SQLHelper:

    def __init__(self):
        os.chdir(os.path.dirname(os.path.realpath(__file__)))       
        self.engine = create_engine("sqlite:///touristtravel.sqlite")

    # Query 0 for line chart - sorting table by the column Total_Travel_Cost To be displayed on Dashboard page
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
    # Query 1 for Bar Chart (-Travel Cost in comparrison to Accomidation )
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

   
    # Query 2 for bar chart - pulling data from table, sorting by the accommodation type
    ## COMPLETE, NEED TO WORK INTO DASHBOARD/app.JS page 
    def query_bubble_data(self):
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
        df2 = pd.read_sql(query, con=conn)

        ##Bubble chart 

        # Sorting the DataFrame by Travel_Count for better visualization
        df2_sorted = df2.sort_values(by='Travel_Count', ascending=False)

        # Create a color map for different modes of transportation
        unique_modes = df2_sorted['Mode_of_Travel'].unique()
        color_map = {mode: plt.cm.tab10(i) for i, mode in enumerate(unique_modes)}

        # Create the bubble chart
        plt.figure(figsize=(8, 8))
        sns.set_style("whitegrid")

        # Plotting the bubbles
        for mode in unique_modes:
            subset = df2_sorted[df2_sorted['Mode_of_Travel'] == mode]
            plt.scatter(subset['Main_Purpose'], subset['Travel_Count'], 
                        s=subset['Travel_Count'] * 20,  # Scale the bubble size
                        color=color_map[mode], alpha=0.6, edgecolor='w', linewidth=0.5, label=mode)

        # Adding labels and title
        plt.xlabel('Main Purpose for Visit', fontsize=14, color='#333333')
        plt.ylabel('Travel Count per the 1000 particpants', fontsize=14, color='#333333')
        plt.title('Travel Count by Main Purpose and Mode of Travel', fontsize=18, color='#333333', pad=20)

        # Rotating the x-axis labels for better readability
        plt.xticks(rotation=45, ha='right', fontsize=12, color='#333333')
        # Adding a custom legend with smaller bubbles
        from matplotlib.lines import Line2D
        legend_elements = [Line2D([0], [0], marker='o', color='w', markerfacecolor=color_map[mode], markersize=10, label=mode) 
                        for mode in unique_modes]
        plt.legend(title='Mode of Travel', handles=legend_elements, fontsize=12, title_fontsize=14)

        # Save the plot as an image file
        plt.savefig('static/images/bubble_chart.png')
    


        plt.tight_layout()
        plt.show()    
            
        conn.close()
        return df2_sorted
    

    # Query 3 Creating the data Table to display on Dashboard page 
    ## INSTERT TABLE ONCE COMPLETED STILL WORKING -BM 02/15/2025
def query_table_data(self, Country_Visited):
    conn = self.engine.connect() # Raw SQL/Pandas
    # Define the SQL query
    query = text("""SELECT
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
    # Use a context manager to ensure the connection is properly closed
    with self.engine.connect() as conn:
        # Execute the query and load the data into a DataFrame
        query = text("""
        SELECT
            Country_Visited,
            Travel_Duration_Days,
            Number_of_Companions,
            Accommodation_Type,
            Main_Purpose,
            Season_of_Visit
        FROM
            touristtravel
        WHERE
            Country_Visited = :country
        """)
        with self.engine.connect() as conn:
            df3 = pd.read_sql(query, con=conn, params={"Country Visited": Country_Visited})
        

    conn.close()
    # Return the DataFrame
    return df3

# Query 4 for pie/donut chart - pulling data from table, sorting by the column Reason_for_Travel(INCOMPLETE)
def query_pie_data(self):
        # Define the SQL query to count occurrences of each Country_Visited
        query = text("""
        SELECT
            Country_Visited,
            COUNT(*) AS Count
        FROM
            touristtravel
        GROUP BY
            Country_Visited
        ORDER BY
            Country_Visited;

        """)

        # Use a context manager to ensure the connection is properly closed
        with self.engine.connect() as conn:
            # Execute the query and load the data into a DataFrame
            df4 = pd.read_sql(query, con=conn)
    
        # Return the DataFrame
        return df4


# Query 5 for Map Data (INCOMPLETE)
# def query_map_data(self):
#     # Run the query and load the data into a DataFrame
