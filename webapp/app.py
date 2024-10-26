import streamlit as st
import plotly.express as px

df = px.data.gapminder()
fig = px.scatter(df, x='gdpPercap', y='lifeExp', trendline='lowess', animation_frame='year')
fig