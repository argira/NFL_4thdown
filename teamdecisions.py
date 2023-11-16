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
  st.header("To Do or Not to Do a 4th down conversion")
  df = data_prep_new() #fourthdown data
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
        keep_columns = ['game_date','play_type','ydstogo','away_team','game_seconds_remaining']
        plot_columns = ['ydsnet','play_type','ydstogo','Decision','home_score','posteam','defteam','game_half','qtr','yardline_100']
        display_df = data[keep_columns]
        display_df = display_df.rename(columns={"game_date": "Date", "play_type": "Play Type", "ydstogo": "Yards to Go"}, errors="raise")
        

        #get key by combining columns
        
        data['game_list'] ='Game Date ' + data['game_date'].astype(str) +" Against "+ data['away_team']
        game_list = list(data['game_list'])


        
        col1,col2 = st.columns(2)

        with col1:
         game = st.selectbox("choose a game",(game_list))
         #st.write("Team "+team+" decisions", display_df.sort_index())
         data = data[data["game_list"]==game]
         data['Decision'] = 'Seconds remaining ' + data['game_seconds_remaining'].astype(str) + ' Yards to go ' + data['ydstogo'].astype(str)
         decisions = list(data['Decision'].unique())

         decision = st.selectbox( "Choose a decision",(decisions))
         
         plot_df = data[plot_columns]
         plot_df = plot_df[plot_df['Decision']==decision]

        with col2:



          plt.figure()
          sns.catplot(data=plot_df,x='play_type', y='ydsnet',kind='box', palette='plasma')
          plt.xticks(rotation=45)
          st.pyplot(plt)

        


  
  team_decisions(df)

  
