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
  st.header("Worst Ten 4th Down decisions by Team and Season")
  df = data_prep() #fourthdown data
  #team_colors = team_colors() #team colors
  


  def bad_decisions(df):
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
        bad_df = data.sort_values(by='ydsnet', ascending=True)
        bad_df = bad_df.head(10)
        keep_columns = ['game_date','away_team','play_type','ydstogo','ydsnet','game_half']
        bad_df = bad_df[keep_columns]
        bad_df = bad_df.rename(columns={"game_date": "Date", "play_type": "Play Type", "ydstogo": "Yards to Go",
                                                'away_team':"Away Team", 'ydsnet':'Yards Net', 'game_half':'Half'}, errors="raise")
        
        st.write("Team "+team+" best decisions", bad_df)

        


  
  bad_decisions(df)
  
