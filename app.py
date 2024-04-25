import pandas as pd
import plotly.express as px
import streamlit as st
def main():
    st.header('This project is a Car Sales Data Spreadsheet Evaluation')
    st.write('It is not a functional application yet. Under construction.')
    st.write('This is a dataframe of Cars being sold. It includes the price,n\model by year, model my type, condition of car, cylinders the car runs on, type of fuel it uses, the amount of miles driven already, type of transmission, how many days its listed to be sold, date posted, paint of car and type of car.')

    # Load data
    cars = pd.read_csv('vehicles_us (1).csv')  # Assuming 'vehicles_us.csv' is in the same directory as your script

    # Create a checkbox to filter data
    new_models = st.checkbox("Show only cars from 2013 or older")
    if new_models:
        cars = cars[cars['model_year'] <= 2013]

    # Create a checkbox to filter expensive cars
    expensive_cars = st.checkbox("Show only cars over $50k")
    if expensive_cars:
        cars = cars[cars['price'] > 50000]

    # Create two columns for displaying the graphs
    col1, col2 = st.columns(2)

    # Display histogram in the first column
    with col1:
        st.subheader('Histogram')
        fig = px.histogram(cars, x='model_year', y='price')
        st.plotly_chart(fig)

    # Display scatter plot in the second column
    with col2:
        st.subheader('Scatter Plot')
        fig2 = px.scatter(cars, x='model_year', y='price')
        st.plotly_chart(fig2)

if __name__ == "__main__":
    main()