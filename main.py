import streamlit as st
# from plotly import express as px
import plotly.express as px
from backend import get_data

# Add the : title, text input, slider, select-box, and sub-header

col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image("Visionary.png")

with col3:
    st.write(' ')

st.title("Joe's Weather Forecast for the Next Days")
place = st.text_input("Place: In any language ")
st.write("Please only select US state if its a US city: ")
state = st.selectbox("Select US state for US city",
                     ("AL", "AK", "AZ", "AR", "AS", "CA", "CO", "CT", "DE",
                      "DC", "FL", "GA", "GU", "HI", "ID", "IL", "IN", "IA",
                      "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS",
                      "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC",
                      "ND", "MP", "OH", "OK", "OR", "PA", "PR", "RI", "SC",
                      "SD", "TN", "TX", "TT", "UT", "VT", "VA", "VI", "WA",
                      "WV", "WI", "WY"))

days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

st.text("Forecast in ascending order : 1 to many days from now.")
st.text("Times : 8AM, 11AM, 2PM, 5PM, 8PM, 11PM, 2AM, 5AM")
# get: temp or sky data

try:
    data = get_data(place=place, forecast_days=days, state=state)
except KeyError:
    st.write("Please enter a location to forecast the weather. ")

# create a : temp or sky plot
try:
    filtered_data = get_data(place=place, forecast_days=days)
    if option == "Temperature":
        temp = [dict['main']['temp'] / 10 for dict in filtered_data]
        # create list compr for days
        dates = [dict["dt_txt"] for dict in filtered_data]
        # Temp plot
        figure = px.line(x=dates, y=temp, labels={"x": "Date", "y": "Temperature (C)"})
        st.plotly_chart(figure)

    if option == "Sky":
        images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                  "Rain": "images/rain.png", "Snow": "images/snow.png"}
        sky_conditions = [dict['weather'][0]['main'] for dict in filtered_data]
        # Translate the filepaths with list comprehension
        img_paths = [images[condition] for condition in sky_conditions]
        st.image(img_paths, width=150)
except KeyError:
    st.write("That place does not exist")
