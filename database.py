import sqlite3
import pandas as pd
from datetime import datetime
def create_database():
    conn = sqlite3.connect("plant_data.db")

    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sensor_data(
            "Simulation ID" TEXT,
            Timestamp TEXT,
            Time INTEGER,
            Temperature REAL,
            Pressure REAL,
            "Flow Rate" REAL,
            "Tank Level" REAL,
            pH REAL,
            Efficiency REAL,
            Energy REAL,
            "Heat Duty" REAL,
            "Operating Cost" REAL
    )
    ''')
    conn.commit()
    conn.close()
def save_sensor_data(df):
    conn = sqlite3.connect("plant_data.db")
    df["Timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    df["Simulation ID"] = datetime.now().strftime("%Y%m%d%H%M%S")
    df.to_sql(
        "sensor_data",
        conn,
        if_exists="append",
        index=False
    )
    conn.commit()
    conn.close()

def load_sensor_data():
    conn = sqlite3.connect("plant_data.db")

    df = pd.read_sql(
        "SELECT * FROM sensor_data",
        conn
    )

    conn.close()

    return df

def clear_database():
    conn = sqlite3.connect("plant_data.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM sensor_data")
    conn.commit()
    conn.close()