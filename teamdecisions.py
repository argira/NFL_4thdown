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


#keep_columns = ['season','home_team','away_team','down','game_date','game_half','game_seconds_remaining', 'play_type', 'ydstogo','yardline_100', 'posteam', 'qtr','side_of_field', 'defteam', 'side_of_field','posteam_score','defteam_score','roof','surface','temp','wind','stadium']
        
        col1,col2 = st.columns(2)

        with col1:
         st.image('images/'+team+'.png')
         game = st.selectbox("choose a game",(game_list))
         #st.write("Team "+team+" decisions", display_df.sort_index())
         data = data[data["game_list"]==game]
         data = data[data['posteam']==team]
         data['Decision'] = 'Quarter ' + data['qtr'].astype(str) + ' Seconds remaining ' + data['game_seconds_remaining'].astype(str) + ' 4th Down and ' + data['ydstogo'].astype(str) + ' yards to go'
         decisions = list(data['Decision'].unique())

         decision = st.selectbox( "Choose a decision",(decisions))
         
         plot_df = data[scoreboard_columns]
         plot_df = plot_df[plot_df['Decision']==decision]

        with col2:

          #st.image('/image'+data['away_team'].astype(str)+'.png') 
          st.markdown("Show the Scoreboard")

          def create_football_field(linenumbers=True,
                          endzones=True,
                          highlight_line=False,
                          highlight_line_number=50,
                          highlighted_name='Line of Scrimmage',
                          fifty_is_los=False,
                          figsize=(12, 6.33)):
            """
             Function that plots the football field for viewing plays.
             Allows for showing or hiding endzones.
            """
            rect = patches.Rectangle((0, 0), 120, 53.3, linewidth=0.1,
                             edgecolor='r', facecolor='darkgreen', zorder=0)
            fig, ax = plt.subplots(1, figsize=figsize)
            ax.add_patch(rect)

            plt.plot([10, 10, 10, 20, 20, 30, 30, 40, 40, 50, 50, 60, 60, 70, 70, 80,
              80, 90, 90, 100, 100, 110, 110, 120, 0, 0, 120, 120],
             [0, 0, 53.3, 53.3, 0, 0, 53.3, 53.3, 0, 0, 53.3, 53.3, 0, 0, 53.3,
              53.3, 0, 0, 53.3, 53.3, 0, 0, 53.3, 53.3, 53.3, 0, 0, 53.3],
             color='white')
            if fifty_is_los:
              plt.plot([60, 60], [0, 53.3], color='gold')
              plt.text(62, 50, '<- Player Yardline at Snap', color='gold')
                # Endzones
            if endzones:
              ez1 = patches.Rectangle((0, 0), 10, 53.3,
                                linewidth=0.1,
                                edgecolor='r',
                                facecolor='blue',
                                alpha=0.2,
                                zorder=0)
              ez2 = patches.Rectangle((110, 0), 120, 53.3,
                                linewidth=0.1,
                                edgecolor='r',
                                facecolor='blue',
                                alpha=0.2,
                                zorder=0)
              ax.add_patch(ez1)
              ax.add_patch(ez2)
              plt.xlim(0, 120)
              plt.ylim(-5, 58.3)
              plt.axis('off')
            if linenumbers:
              for x in range(20, 110, 10):
                numb = x
              if x > 50:
                numb = 120 - x
                plt.text(x, 5, str(numb - 10),
                     horizontalalignment='center',
                     fontsize=20,  # fontname='Arial',
                     color='white')
                plt.text(x - 0.95, 53.3 - 5, str(numb - 10),
                     horizontalalignment='center',
                     fontsize=20,  # fontname='Arial',
                     color='white', rotation=180)
            if endzones:
              hash_range = range(11, 110)
            else:
              hash_range = range(1, 120)

              for x in hash_range:
                ax.plot([x, x], [0.4, 0.7], color='white')
                ax.plot([x, x], [53.0, 52.5], color='white')
                ax.plot([x, x], [22.91, 23.57], color='white')
                ax.plot([x, x], [29.73, 30.39], color='white')

            if highlight_line:
              hl = highlight_line_number + 10
              plt.plot([hl, hl], [0, 53.3], color='yellow')
              # plt.text(hl + 2, 50, '<- {}'.format(highlighted_name),
              #          color='yellow')
            return fig, ax

          #plt.figure()
          #sns.catplot(data=plot_df,x='play_type', y='ydsnet',kind='box', palette='plasma')
          #plt.xticks(rotation=45)
          #st.pyplot(plt)

        


  
  team_decisions(df)

  

  
