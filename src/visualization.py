from matplotlib import pyplot as plt
from matplotlib.figure import Figure as plt_figure
import plotly.express as px
from plotly.graph_objs._figure import Figure as px_figure
import pandas as pd
from wordcloud import WordCloud, STOPWORDS


def create_histogram(
    data: pd.DataFrame, variable: str, title: str, xaxis: str, yaxis: str
) -> px_figure:
    """
    Creates a histogram from a DataFrame using Plotly Express.

    Parameters:
    - data (pd.DataFrame): The DataFrame containing the data to be plotted.
    - variable (str): The column name in `data` to be used for the
      histogram's x-values.
    - title (str): The title of the histogram.
    - xaxis (str): The label for the x-axis.
    - yaxis (str): The label for the y-axis.

    Returns:
    - plotly.graph_objs._figure.Figure: A Plotly Figure object representing
      the histogram.
    """

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
    """
    Generates an interactive count plot for a specified column in a DataFrame.

    Parameters:
    - data (pd.DataFrame): DataFrame containing data.
    - variable (str): Column name for count plot.
    - title (str): Plot title.
    - xaxis (str): X-axis label.
    - yaxis (str): Y-axis label.

    Returns:
    - plotly.graph_objs._figure.Figure: A Plotly Figure object
      of the histogram.
    """

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
    """
    Generates a word cloud from the provided text.

    Parameters:
    - text (str): Text from which to generate the word cloud.

    Returns:
    - matplotlib.figure.Figure: A Matplotlib figure object with the word cloud.
    """

    wordcloud = WordCloud(
        width=800, height=300, stopwords=STOPWORDS, background_color="white"
    ).generate(text)

    # create word cloud with matplotlib
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")

    return fig
