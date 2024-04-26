import plotly.express as px
import pandas as pd


def create_histogram(data: pd.Series, title: str):
    return px.histogram(data, title=title)
