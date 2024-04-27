import plotly.express as px
from plotly.graph_objs._figure import Figure
import pandas as pd


def create_histogram(
    data: pd.DataFrame, variable: str, title: str, xaxis: str, yaxis: str
) -> Figure:
    fig = px.histogram(data, x=variable)

    # format figure
    fig.update_layout(
        title={
            "text": title,
            "y": 0.9,
            "x": 0.5,
            "xanchor": "center",
            "yanchor": "top",
            "font": {"size": 24},
        },
        showlegend=False,
        xaxis_title=xaxis,
        yaxis_title=yaxis,
    )

    return fig


def create_countplot(
    data: pd.DataFrame, variable: str, title: str, xaxis: str, yaxis: str
) -> Figure:
    fig = px.histogram(data, x=variable, text_auto=True)

    # format figure
    fig.update_layout(
        title={
            "text": title,
            "y": 0.9,
            "x": 0.5,
            "xanchor": "center",
            "yanchor": "top",
            "font": {"size": 24},
        },
        showlegend=False,
        xaxis_title=xaxis,
        yaxis_title=yaxis,
        bargap=0.2,
    )
    fig.update_traces(
        textfont_size=12, textangle=0, textposition="outside", cliponaxis=False
    )

    return fig
