import pandas as pd

import streamlit as st

import plotly.express as px

st.header('Introduction: This is a dataframe of Cars being sold.') 
st.write('It includes the price, model by year, model my type, and condition of car.')
st.write('As well as the  cylinders the car runs on, type of fuel it uses, and the amount of miles driven already.') 
st.write('Also type of transmission, how many days its been listed to be sold, date posted, paint of car and type of car is posted.') 

st.write('The file contains no duplicates but does have alot of missing values in is_4wd paint_color, \
          odometer, cylinders, and model_year.')

st.write('Conclusion: Based on the charts usually, the more recent a car was made the more you pay for it.')

# Load data
cars = pd.read_csv(r'C:\Users\tonyr\steve\repo2\vehicles_us (1).csv')

# Create a checkbox to filter data
new_models = st.checkbox("Show only cars from 2013 or older")

if new_models:
    cars = cars[cars['model_year'] <= 2013]

# Create a checkbox to filter expensive cars
expensivecars = st.checkbox("Show only cars over $50k")

if expensivecars:
    cars = cars[cars['price'] > 50000]

# Create two columns for displaying the graphs
col1, col2 = st.columns(2)

# Display histogram in the first column
with col1:
    st.subheader('Histogram')
    fig = px.histogram(cars, x='model_year', y='price')
    fig.update_layout(xaxis_title='Model Year', yaxis_title='Price')
    fig.update_layout(title = 'Car Sales Histogram')
    st.plotly_chart(fig)

# Display scatter plot in the second column
with col2:
    st.subheader('Scatter Plot')
    fig2 = px.scatter(cars, x='model_year', y='price')
    fig2.update_layout(xaxis_title='Model Year', yaxis_title='Price')
    fig2.update_layout(title = 'Car Sales Scatter Plot')
    st.plotly_chart(fig2)

if __name__ == "__main__":
    main()