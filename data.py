import numpy as np
import pandas as pd
from calculations import (
    calculate_efficiency,
    calculate_heat_duty,
    calculate_energy,
    calculate_operating_cost
)
def generate_sensor_data(
        temperature,
        pressure,
        flow_rate,
        pH,
        Tank_level,
        n = 100
):
    time = np.arange(n)
    temperature_data = np.random.normal(
        temperature,   #mean
        2,  #standard deviation
        n   #num of values
    )
    pressure_data = np.random.normal(
        pressure,
        15,
        n
    )
    flow_data = np.random.normal(
        flow_rate,
        5,
        n
    )
    pH_data = np.random.normal(
        pH,
        0.05,
        n
    )
    Tank_level_data = np.random.normal(
        Tank_level,
        3,
        n
    )
    df = pd.DataFrame({
        "Time": time,
        "Temperature": temperature_data,
        "Pressure": pressure_data,
        "Flow Rate": flow_data,
        "Tank level": Tank_level_data,
        "pH": pH_data
    })
    return df

def calculate_sensor_parameters(df):
    df["Efficiency"] = calculate_efficiency(df["Temperature"],
                                            df["Pressure"])
    df["Energy"] = calculate_energy(df["Temperature"],
                                     df["Flow Rate"])
    df["Heat Duty"] = calculate_heat_duty(df["Temperature"],
                                          df["Flow Rate"])
    df["Operating Cost"] = calculate_operating_cost(df["Energy"])

    return df
