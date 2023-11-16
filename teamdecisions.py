import streamlit as st
import numpy as py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#import statsmodels.formula.api as sm
import altair as alt
from load_data import data_prep
#from load_data import team_logos
from scipy import stats
#from helpers import pearsonr_ci


def app():
  st.header("To Do or Not to Do a 4th down conversion")
  df = data_prep() #fourthdown data
  #logos = team_logos()
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
    #logo = logos[logos['team']==team]
    #l = logos['team_logo'].astype(str)
    

    if not team: st.error("Please select a team.")
    else:
      if not season:st.error("Please select a season")
      else:
        data = df[df["home_team"]==team]
        data = data[data["season"]==season]
        keep_columns = ['game_date','play_type','ydstogo','away_team','game_seconds_remaining']
        scoreboard_columns = ['away_team','play_type','ydstogo','Decision','game_seconds_remaining','game_half','yardline_100','qtr','side_of_field','posteam_score','defteam_score']
        display_df = data[keep_columns]
        display_df = display_df.rename(columns={"game_date": "Date", "play_type": "Play Type", "ydstogo": "Yards to Go"}, errors="raise")
        

        #get key by combining columns
        
        data['game_list'] ='Game Date ' + data['game_date'].astype(str) +" Against "+ data['away_team']
        game_list = list(data['game_list'].unique())
        game = st.selectbox("choose a game",(game_list))
         #st.write("Team "+team+" decisions", display_df.sort_index())
         
        data = data[data["game_list"]==game]
        against_team = list(data['away_team'].unique()) 
        data = data[data['posteam']==team]


#keep_columns = ['season','home_team','away_team','down','game_date','game_half','game_seconds_remaining', 'play_type', 'ydstogo','yardline_100', 'posteam', 'qtr','side_of_field', 'defteam', 'side_of_field','posteam_score','defteam_score','roof','surface','temp','wind','stadium']
        
        col1,col2 = st.columns(2)

        with col1:
         st.image('images/'+team+'.png')
         
         data['Decision'] = 'Quarter ' + data['qtr'].astype(str) + ' Seconds remaining ' + data['game_seconds_remaining'].astype(str) + ' 4th Down and ' + data['ydstogo'].astype(str) + ' yards to go'
         decisions = list(data['Decision'].unique())

         decision = st.selectbox( "Choose a decision",(decisions))
         
         plot_df = data[scoreboard_columns]
         plot_df = plot_df[plot_df['Decision']==decision]

        with col2:

          st.image('/image'+ ' '.join(against_team) +'.png') 
          st.markdown("Show the Scoreboard")

          

          #plt.figure()
          #sns.catplot(data=plot_df,x='play_type', y='ydsnet',kind='box', palette='plasma')
          #plt.xticks(rotation=45)
          #st.pyplot(plt)

        


  
  team_decisions(df)

  

  
