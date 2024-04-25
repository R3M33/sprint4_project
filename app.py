import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.header('Tossing a Coin')
    st.write('It is not a functional application yet. Under construction.')

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