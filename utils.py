def check_plant_status(df):

    alerts = []

    if df["Temperature"].max() > 105:
        alerts.append("🌡️ High Temperature")

    if df["Pressure"].max() > 1030:
        alerts.append("⚠️ High Pressure")

    if df["Tank level"].min() < 70:
        alerts.append("🛢️ Low Tank Level")

    if df["pH"].min() < 6.8 or df["pH"].max() > 7.2:
        alerts.append("🧪 Abnormal pH")

    return alerts

def check_plant_status(
    df,
    temp_limit,
    pressure_limit
):
    alerts = []

    if df["Temperature"].max() > temp_limit:
        alerts.append("🌡️ High Temperature")

    if df["Pressure"].max() > pressure_limit:
        alerts.append("⚠️ High Pressure")

    if df["Tank level"].min() < 70:
        alerts.append("🛢️ Low Tank Level")

    if df["pH"].min() < 6.8 or df["pH"].max() > 7.2:
        alerts.append("🧪 Abnormal pH")

    return alerts
        