from sqlalchemy import create_engine, text
import pandas as pd




class sqlhelper():


    def __init__(self):
        self.engine = create_engine("sqlite:///touristtravel.sqlite")
# Querry 1 for line chart- sorting table by the column Total_Travel_Cost
    def querylineData(self):
        # Create our session (link) from Python to the DB
        conn = self.engine.connect()  # Raw SQL/Pandas
        # Define Query
        query = text("""SELECT *
                        FROM touristtravel
                        ORDER BY Total_Travel_Cost ASC""")
        df = pd.read_sql(query, con=conn)

        # Close the connection
        conn.close()
        return df
     
#Query 2 for Barchart, pull data from table sorting from the accomidation type 
   def querybarData(self):
        # Create our session (link) from Python to the DB
        conn = self.engine.connect()  # Raw SQL/Pandas
        # Define Query
        query = text("""SELECT *
                        FROM touristtravel
                        ORDER BY """)
        df = pd.read_sql(query, con=conn)

        # Close the connection
        conn.close()
        return 

#Query 3 for pie/donut chart, pull data from table sorting by the column Reason for Travel 
   def querypieData(self):
        # Create our session (link) from Python to the DB
        conn = self.engine.connect()  # Raw SQL/Pandas
        # Define Query
        query = text("""SELECT *
                        FROM touristtravel
                        ORDER BY """)
        df = pd.read_sql(query, con=conn)

        # Close the connection
        conn.close()
        return 