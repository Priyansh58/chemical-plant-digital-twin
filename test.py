from data import (generate_sensor_data,
                  calculate_sensor_parameters)

df = generate_sensor_data(
    temperature=100,
    pressure=1000,
    flow_rate=250,
    pH=7,
    Tank_level=80
)
df = calculate_sensor_parameters(df)
print(df.head())