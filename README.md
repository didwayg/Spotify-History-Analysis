# Spotify Listening Analysis and Recommendation Tool
### Course Project Overview
This repository contains my Data Science course project at Whitman College. The project aims to analyze my own music listening history and to develop a tool for generating a personalized playlist with recommended songs.

### Project Files
gather_personal_data.py: Gathers personal music listening history data. This script is run first to collect and format streaming data.
preprocessing.ipynb: A Jupyter notebook for preprocessing the gathered data, preparing it for analysis and recommendation. Retrieves and organizes information about songs and artists.
analysis.ipynb: Performs exploratory data analysis on my music listening history, uncovering insights and trends in my music preferences.
my_music_recommender.ipynb: Utilizes the preprocessed data to create a personalized playlist of recommended songs based on my listening history.
spotify_api_functions.py: Contains functions for Spotipy API calls used in both the preprocessing and recommendation process.
### Workflow
The workflow of the project is as follows:

Run gather_personal_data.py to collect and prepare my streaming history.
Execute preprocessing.ipynb for data cleaning and transformation.
Analyze the data with analysis.ipynb to understand music preferences and trends.
Use my_music_recommender.ipynb to generate a personalized playlist with song recommendations.
### Setup and Installation
Ensure you have Python installed along with necessary libraries like pandas, numpy, matplotlib, seaborn, and scikit-learn. Additionally, you'll need to install Spotipy for Spotify API interactions.

You can install these dependencies using pip:

      pip install pandas numpy matplotlib seaborn scikit-learn spotipy

### Usage
Follow the workflow steps to go from raw data collection to generating a personalized playlist. Ensure to have your Spotify API credentials set up for the Spotipy functions to work.

### Contribution and Feedback
I welcome any feedback or suggestions from you all.
