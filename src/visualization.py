from matplotlib import pyplot as plt
from matplotlib.figure import Figure as plt_figure
import plotly.express as px
from plotly.graph_objs._figure import Figure as px_figure
import pandas as pd
from wordcloud import WordCloud, STOPWORDS


def create_histogram(
    data: pd.DataFrame, variable: str, title: str, xaxis: str, yaxis: str
) -> px_figure:
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
) -> px_figure:
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


def create_word_cloud(text: str) -> plt_figure:

    wordcloud = WordCloud(
        width=800, height=300, stopwords=STOPWORDS, background_color="white"
    ).generate(text)

    # create word cloud with matplotlib
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    
    return fig
