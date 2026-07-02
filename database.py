import sqlite3
import pandas as pd
from datetime import datetime
import uuid
def create_database():
    conn = sqlite3.connect("plant_data.db")

    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sensor_data(
            SimulationID TEXT,
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
    simulation_id = str(uuid.uuid4())[:8]
    timestamp = datetime.now().strftime(
        "%d-%m-%Y %H:%M:%S"
    )
    df["SimulationID"] = simulation_id
    df["Timestamp"] = timestamp
    
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