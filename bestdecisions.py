import streamlit as st
from streamlit_d3graph import d3graph
import numpy as py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#import statsmodels.formula.api as sm
import altair as alt
from load_data import data_prep_new
from load_data import team_colors
from scipy import stats
#from helpers import pearsonr_ci


def app():
  st.header("Top Ten 4th down decisions by team and season")
  df = data_prep_new() #fourthdown data
  #team_colors = team_colors() #team colors

  

# Initialize
d3 = d3graph()
# Load karate example
adjmat, df = d3.import_example('karate')

label = df['label'].values
node_size = df['degree'].values

d3.graph(adjmat)
d3.set_node_properties(color=df['label'].values)
d3.show()

d3.set_node_properties(label=label, color=label, cmap='Set1')
d3.show()
  


  #def best_decisions(df):
  #  teams = list(df["home_team"].unique())
  #  teams.sort()
  #  seasons = list(df['season'].unique())
  #  seasons.sort()
  #  team = st.selectbox(
  #    "Select a Team",
  #    (teams))
  #  season = st.selectbox( "Select a Season",
  #    (seasons)
  #  )
    
  #  if not team: st.error("Please select a team.")
  #  else:
  #    if not season:st.error("Please select a season")
  #    else:
  #      data = df[df["home_team"]==team]
  #      data = data[data["season"]==season]
  #      best_df = data.sort_values(by='ydsnet', ascending=False)
  #      best_df = best_df.head(10)
  #      keep_columns = ['game_date','away_team','play_type','ydstogo','ydsnet','game_half']
  #      best_df = best_df[keep_columns]
  #      best_df = best_df.rename(columns={"game_date": "Date", "play_type": "Play Type", "ydstogo": "Yards to Go",
  #                                              'away_team':"Away Team", 'ydsnet':'Yards Net', 'game_half':'Half'}, errors="raise")
        
  #      st.write("Team "+team+" best decisions", best_df)

        


  
  #best_decisions(df)
  
