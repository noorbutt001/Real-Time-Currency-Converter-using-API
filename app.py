import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from services.weather_service import WeatherService
from services.alert_service import AlertService

st.set_page_config(
    page_title="Weather Dashboard",
    layout="wide"
)

st.title(
    "Advanced Weather Tracking Dashboard"
)

cities = st.multiselect(
    "Select Cities",
    [
        "Lahore",
        "Karachi",
        "Islamabad",
        "Dubai",
        "London"
    ]
)

service = WeatherService()

all_data = []

for city in cities:

    weather = service.get_weather(city)

    if "error" not in weather:

        st.subheader(city)

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Temperature",
            f"{weather['temperature']} °C"
        )

        col2.metric(
            "Humidity",
            weather["humidity"]
        )

        col3.metric(
            "Wind Speed",
            weather["wind_speed"]
        )

        alerts = AlertService.get_alerts(
            weather
        )

        for alert in alerts:
            st.warning(alert)

        all_data.append(weather)

if all_data:

    df = pd.DataFrame(all_data)

    st.dataframe(df)

    fig, ax = plt.subplots()

    ax.plot(
        df["city"],
        df["temperature"]
    )

    st.pyplot(fig)