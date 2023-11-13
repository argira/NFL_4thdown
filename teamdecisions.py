import streamlit as st
import numpy as py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#import statsmodels.formula.api as sm
import altair as alt
from load_data import data_prep
#from load_data import team_colors
from scipy import stats
#from helpers import pearsonr_ci


def app():
  st.header("To Do or Not to Do a 4th down conversion")
  df = data_prep() #fourthdown data
  #team_colors = team_colors() #team colors
  


  def team_decisions(df):
    teams = list(df["home_team"].unique())
    teams.sort()
    seasons = list(df['season'].unique())
    seasons.sort()
    team = st.selectbox(
      "Select a Team",
      (teams))
    season = st.selectbox( "Select a Season",
      (seasons)
    )
    
    if not team: st.error("Please select a team.")
    else:
      if not season:st.error("Please select a season")
      else:
        data = df[df["home_team"]==team]
        data = data[data["season"]==season]
        keep_columns = ['home_team','away_team','down','game_date','game_half','game_seconds_remaining', 'play_type', 'ydstogo','yardline_100']
        display_df = data[keep_columns]
        st.write("Team "+team+" decisions", display_df.sort_index())

        


  
  team_decisions(df)
  
