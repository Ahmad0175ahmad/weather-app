# weather_streamlit.py

import streamlit as st
import requests

API_KEY = "169fa8b1434b7a02616e3317f26ab164"

st.title("🌦️ Weather App")

city = st.text_input("Enter city name")

if st.button("Get Weather"):
    if not city:
        st.warning("Please enter a city name.")
    else:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            temp = data["main"]["temp"]
            condition = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]

            st.success(f"Weather in {city.capitalize()}")
            st.write(f"🌡️ Temperature: {temp}°C")
            st.write(f"☁️ Condition: {condition.capitalize()}")
            st.write(f"💧 Humidity: {humidity}%")
        else:
            st.error(f"❌ Error: {data.get('message', 'Unknown error')}")
