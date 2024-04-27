import plotly.express as px
from plotly.graph_objs._figure import Figure
import pandas as pd


def create_histogram(data: pd.Series, title: str) -> Figure:
    return px.histogram(data, title=title)


def create_countplot(data: pd.DataFrame, variable: str, title: str) -> Figure:
    fig = px.histogram(data, x=variable, title=title, text_auto=True)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    fig.update_layout(bargap=0.2)
    return fig
