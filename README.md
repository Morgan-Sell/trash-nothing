![Garden created from trash](img/garden.png)

# Trash Nothing Dashboard: Life Trends of Second-Hand Goods

## Project Overview
This project asynchronously retrieves data from [Trash Nothing](https://trashnothing.com/beta/browse?r=logo) API then leverages Python's dataclass
to process and store the data in a CSV file. Once the data is saved, the application loads the data and performs additional processing. The 
application then generates a dashboard that provides both numerical and text analyses.

TrashPost is a website in which people offer second-hand goods to others, predominantly for free. A post includes a title, description, day/time available for pickup, location, and more. A post also includes whether the item was picked up.

## Installation
Follow these steps to install and use the Trash Nothing Dashboard:

1. **Clone the Repository**: Start by cloning this repository to your local machine:
   
    ```bash
    git clone https://github.com/Morgan-Sell/trash-nothing.git
    ```

2. **Install Dependencies**: Navigate into the project directory and install the required dependencies using pip:

    ```bash
    cd trash-nothing
    pip install -r requirements.txt
    ```

3. **Set Up API Key**: You'll need an API key from Trash Nothing to access their API. If you don't have one already, sign up for an account on [Trash Nothing](https://www.trashnothing.com) and generate an API key.

4. **Configure API Key**: Once you have your API key, create a `.env` file in the root directory of the project. Add your API key to this file in the following format:

    ```plaintext
   API_KEY=your_api_key_here
    ```
5. **Save and Close**: Save the `.env` file and close it.
   
6. **Gain Access to Groups Data**: To access group data, which provides a much richer dataset, you must join a TrashNothing group. Once you join the group, ask the group administrator for the group ID. You can join more than one group.
   
7. **Update Config File**: When you obtain the group ID(s), update the `group_ids` key in the `API_PARAMS` on the `config.py` file. Currently, the group ID is `4673`, which corresponds to the DC ReUse It group.

## Dashboard Samples

Here are a few sample visualizations from the Trash Nothing dashboard.

In the below word cloud, we see the words that are most used in the post descriptions. Understandably, the primary words correspond to (1) coordination/exchange guidelines, e.g., policy, offer, pick up, and (2) general product descriptions, e.g., good condition, old, and size.

<p align="center">
    <img src="img/wordcloud.png" alt="Posts Description Word Cloud">
</p>


The below count plot shows the number of items that are still available or have been promised to an individual. This visualization is misleading because it does not show the items that were taken. Once an item is taken, the users remove it from the site.


<p align="center">
    <img src="img/outcome.png" alt="Outcome Distribution">
</p>


Another interesting observation is how long do people make their items available pickup. We nearly see a binomial distribution with the apexes at 10 - 20 days and 80 - 90 days. We are unsure of the default settings. The 3 month duration may be caused by default bias.


<p align="center">
    <img src="img/days_available.png" alt="Days Available">
</p>


## Project Structure

```
TRASH_NOTHING/
│
├── data/  # hidden from GitHub. demonstrates where data is stored.
│ └── trash_posts.csv
│
├── img/
│ ├── days_available.png
│ ├── garden.png
│ ├── interest.png
│ ├── outcome.png
│ ├── recycle.png
│ └── wordcloud.png
│
├── src/
│ ├── init.py
│ ├── api.py
│ ├── app.py
│ ├── config.py
│ ├── data_processing.py
│ ├── models.py
│ └── visualization.py
│
├── tests/
│ ├── init.py
│ ├── conftest.py
│ ├── test_api.py
│ ├── test_data_processing.py
│ └── test_models.py
│
├── .gitignore
├── LICENSE
├── project.toml
├── README.md
├── requirements.txt
└── LICENSE

```
### Explanation

- `data/`: Contains CSV files used for data processing.
- `img/`: Holds images used in the project for documentation or analysis.
- `src/`: Source code including the main application and utility modules.
- `tests/`: Contains unit tests for testing the source code.
- `world-pop-env/`: Python virtual environment for managing dependencies.

## Project Inspiration
I developed the Trash Nothing dashboard as a final project for [ArjanCodes Next-Level Python](https://www.arjancodes.com/courses/nlp/). My goal for the project was to implement Python's dataclass and concurrent programming.

## Packages
- pandas
- streamlit
- aiohttp
- plotly.express
- wordcloud
- matplotlib
- pytest
- pytest-asyncio
- pytest-mock
- pytest-aiohttp
- black
- isort
- python-dotenv
- setuptools
- flake8
