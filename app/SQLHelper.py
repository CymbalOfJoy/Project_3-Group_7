from sqlalchemy import create_engine, text
import pandas as pd


class SQLHelper:

    def __init__(self):
        self.engine = create_engine("sqlite:///touristtravel.sqlite")

    # Query 1 for line chart - sorting table by the column Total_Travel_Cost
    def query_line_data(self):
        conn = self.engine.connect()  # Raw SQL/Pandas
        query = text("""SELECT *
                        FROM touristtravel
                        ORDER BY Total_Travel_Cost ASC""")
        df = pd.read_sql(query, con=conn)
        conn.close()
        return df

    # Query 2 for bar chart - pulling data from table, sorting by the accommodation type
    def query_bar_data(self):
        conn = self.engine.connect()  # Raw SQL/Pandas
        query = text("""SELECT *
                        FROM touristtravel
                        ORDER BY Mode_of_Travel""")
        df = pd.read_sql(query, con=conn)
        conn.close()
        return df

    # Query 3 for pie/donut chart - pulling data from table, sorting by the column Reason_for_Travel
    def query_pie_data(self):
        conn = self.engine.connect()  # Raw SQL/Pandas
        query = text("""SELECT *
                        FROM touristtravel
                        ORDER BY Reason_for_Travel""")
        df = pd.read_sql(query, con=conn)
        conn.close()
        return