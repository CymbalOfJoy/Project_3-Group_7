from sqlalchemy import create_engine, text
import pandas as pd

class sqlhelper():
    def __init__(self):
        self.engine = create_engine("sqlite:///touristtravel.sqllite")

conn = self.engine.connect()

