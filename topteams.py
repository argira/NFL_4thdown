import streamlit as st
import numpy as py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#import statsmodels.formula.api as sm
import altair as alt
from load_data import data_prep_new
#from load_data import team_colors
from scipy import stats
#from helpers import pearsonr_ci


def app():
  st.header("Top 4th Down Performers")
  df = data_prep_new() #fourthdown data
  #team_colors = team_colors() #team colors
  


  def top_performers(df):
        
    teams = df.groupby("home_team").sum("ydsnet").sort_values(by='ydsnet', ascending=False).head(10)
    teams = teams['home_team']
    #teams = list(df["home_team"].unique())
    #teams.sort()
    #seasons = list(df['season'].unique())
    #seasons.sort()
    #team = st.selectbox(
     # "Select a Team",
     # (teams))
    #season = st.selectbox( "Select a Season",
     # (seasons)
   # )
    
    #if not team: st.error("Please select a team.")
    #else:
     # if not season:st.error("Please select a season")
      #else:
        #data = df[df["home_team"]==team]
        #data = data[data["season"]==season]
        #top_df = df.sort_values(by='ydsnet', ascending=False)
        #top_df = top_df.head(10)
        #keep_columns = ['game_date','away_team','play_type','ydstogo','ydsnet','game_half']
        #top_df = top_df[keep_columns]
    teams = teams.rename(columns={'home_team':"Team"}, errors="raise")
        
    st.write("Top 4th down Performers ", teams)

        


  
  top_performers(df)
  
