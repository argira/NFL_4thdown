import streamlit as st
import numpy as py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#import statsmodels.formula.api as sm
import altair as alt
from load_data import data_prep
from footballfield import create_football_field
from load_data import team_colors
from load_data import all_data
from scipy import stats
#from helpers import pearsonr_ci


def app():
  st.header("Win Probability based on 4th down decision")
  df = data_prep() #fourthdown data
  #logos = team_logos()
  teamcolors = team_colors() #team colors
  all_df = all_data()
  


  


  def team_decisions(df):
    cola, colb = st.columns([3,10])
    with cola:
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
    
    
    with colb:

      if not team: st.error("Please select a team.")
      else:
        if not season:st.error("Please select a season")
        else:
          data = df[df["home_team"]==team]
          data = data[data["season"]==season]
          #keep_columns = ['game_id','game_date','play_type','ydstogo','away_team','game_seconds_remaining']
          #scoreboard_columns = ['qtr' , 'yardline_100' , 'play_type' , 'ydstogo' , 'game_seconds_remaining' , 'game_half' , 'side_of_field','posteam_score','defteam_score']
          #display_df = data[keep_columns]
          #display_df = display_df.rename(columns={"game_date": "Date", "play_type": "Play Type", "ydstogo": "Yards to Go"}, errors="raise")
        

        #get key by combining columns
        
          data['game_list'] ='Game Date ' + data['game_date'].astype(str) +" Against "+ data['away_team']
          game_list = list(data['game_list'].unique())
          game = st.selectbox("choose a game",(game_list))
          #st.write("Team "+team+" decisions", display_df.sort_index())
         
          data = data[data["game_list"]==game]
          game_id = list(data['game_id'].unique())
          against_team = list(data['away_team'].unique()) 
          data = data[data['posteam']==team]


#keep_columns = ['season','home_team','away_team','down','game_date','game_half','game_seconds_remaining', 'play_type', 'ydstogo','yardline_100', 'posteam', 'qtr','side_of_field', 'defteam', 'side_of_field','posteam_score','defteam_score','roof','surface','temp','wind','stadium']
        
         # col1,col2 = st.columns(2)

          #with col1:
            #st.image('images/'+team+'.png')
         
    data['Decision'] = 'Quarter ' + data['qtr'].astype(str) + ' Seconds remaining ' + data['game_seconds_remaining'].astype(str) + ' 4th Down and ' + data['ydstogo'].astype(str) + ' yards to go'
    decisions = list(data['Decision'].unique()) 

         # with col2:

          #  st.image('images/'+' '.join(against_team) +'.png') 
          #st.markdown("Show the Scoreboard")
    decision = st.selectbox( "Choose a play",(decisions))
         
    plot_df = data[data['Decision']==decision]
    #plot_df = plot_df[scoreboard_columns]

    colA,colB,colC = st.columns(3)

    with colA:
      logA, logB = st.columns(2)
      with logA:
        st.image('images/'+team+'.png')
      with logB:
        pt_score = plot_df['posteam_score'].astype(int).astype(str)
        st.subheader('Score')
        score_pos = '<p style="font-family:sans-serif; color:Yellow; font-size: 58px;">'+ ''.join(pt_score)+' </p>'
        st.markdown(score_pos, unsafe_allow_html=True)
       
    with colB:
      st.subheader("Game Status")
      score1,score2,score3 = st.columns(3)
      with score1:
        st.markdown('Quarter')
        quarter = plot_df['qtr'].astype(str)
        quarter_info =  '<p style="font-family:sans-serif; color:blue; font-size: 30px; alignment:center;">'+ ''.join(quarter)+' </p>'
        st.markdown(quarter_info, unsafe_allow_html=True)
      with score2:
        st.markdown('Ball on')
        yard_line = plot_df['yardline_100'].astype(int).astype(str)
        yard_info =  '<p style="font-family:sans-serif; color:blue; font-size: 30px;alignment:center;">'+ ''.join(yard_line)+' </p>'
        st.markdown(yard_info, unsafe_allow_html=True)
      with score3:
        st.markdown('Yds to Go')
        ydstogo = plot_df['ydstogo'].astype(str)
        quarter_info =  '<p style="font-family:sans-serif; color:blue; font-size: 30px;alignment:center;">'+ ''.join(ydstogo)+' </p>'
        st.markdown(quarter_info, unsafe_allow_html=True)








    with colC:
      away1, away2 = st.columns(2)
      with away1:
        st.image('images/'+' '.join(against_team) +'.png')
      with away2:
        dt_score = plot_df['defteam_score'].astype(int).astype(str)
        st.subheader('Score')
        score_def = '<p style="font-family:sans-serif; color:Yellow; font-size: 58px;">'+ ''.join(dt_score)+' </p>'
        st.markdown(score_def, unsafe_allow_html=True)
        

    
    #color_pos = teamcolors[teamcolors['team']==team]
    #colorA = color_pos['color'].astype(str)      

    #plt.figure()
    #sns.lineplot(data=game_df, palette="tab10", linewidth=2.5)
    #sns.catplot(data=data,x='play_type', y='ydstogo',kind='box', palette='plasma')
    #plt.xticks(rotation=45)
    #st.pyplot(plt)
    #plt.figure()


       

    game_df = all_df[all_df['game_id']==game_id[0]]
    team1 = list(plot_df['home_team'].unique())
    team2 = list(plot_df['away_team'].unique())
    game_teams = [team1[0],team2[0]]

    cols_graphic = ['home_wp','away_wp','game_seconds_remaining']


     
    colors = []
    for t in game_teams:
      colors.append(teamcolors[teamcolors["team"]==t]['color'].tolist()[0])

    graph_data = game_df[cols_graphic].set_index("game_seconds_remaining").sort_index(ascending=True).rename(columns={"home_wp":game_teams[0],
                                "away_wp":game_teams[1]})

    tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
    tab1.write("this is tab 1")
    tab2.write("this is tab 2")

    with tab1:
      plt.figure()

      yl=yard_line.astype(int)
      yt=ydstogo.astype(int)
      fig, ax = create_football_field(highlight_line=True,
                                highlight_line_number=yl, yards_to_go=yt)

      plt.xlim(0, 120)
      plt.ylim(0, 53.5)
      plt.vlines(x=yl+yt,
           ymin=-5,
           ymax=58.3,
           colors=["yellow","yellow"],
           linestyles="dashed",
           linewidth=2)#"dashed"

      plt.text(5, 25, game_teams[0],
         size="x-large", 
         rotation=90,
         color="white")

      plt.text(112, 25, game_teams[1],
         size="x-large", 
         rotation=270,
         color="white")
    
      st.pyplot(plt)
      plt.figure() 

  

    with tab2:

      plt.figure()
      sns.lineplot(data=graph_data, palette=colors, linewidth=1.5)
    #sns.catplot(data=data,x='play_type', y='ydstogo',kind='box', palette='plasma')
      plt.xticks(rotation=45)
      plt.xlabel("Time Remaining (seconds)")
      plt.ylabel("Win Probability")
      plt.title(f"Win Probability Chart\n{game_teams[0]} vs {game_teams[1]}")
      st.pyplot(plt)
      plt.figure()

    #display(graph_data.head())
    #graph_data.plot(color=colors)
    #plt.xlabel("Time Remaining (seconds)")
    #plt.ylabel("Win Probability")
    #plt.title(f"Win Probability Chart\n{teams[0]} vs {teams[1]}")
    #plt.gca().invert_xaxis()
    
  
  team_decisions(df)
  #plt.show()

  

  
