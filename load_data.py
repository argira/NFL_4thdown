import numpy as np
from pathlib import Path
import sys
import datetime as dt

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import streamlit as st

@st.cache_data
def data_prep():

  #df = pd.read_csv("data/data_pre.csv")
  df1 = pd.read_csv("data/final_data_2009.csv")
  df2 = pd.read_csv("data/final_data_2010.csv")
  df3 = pd.read_csv("data/final_data_2011.csv")
  df4 = pd.read_csv("data/final_data_2012.csv")
  df5 = pd.read_csv("data/final_data_2013.csv")
  df6 = pd.read_csv("data/final_data_2014.csv")
  df7 = pd.read_csv("data/final_data_2015.csv")
  df8 = pd.read_csv("data/final_data_2016.csv")
  df9 = pd.read_csv("data/final_data_2017.csv")
  df10 = pd.read_csv("data/final_data_2018.csv")
  df11 = pd.read_csv("data/final_data_2019.csv")

  df = pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11])
  return df
#@st.cache_data
#def data_prep_new():
 # df = pd.read_csv("data/new_data_team.csv")
 
# return df
@st.cache_data

def team_colors():
    team_colors = pd.read_csv("data/teamcolors.csv")
    return team_colors

@st.cache_data

def team_logos():
    team_logos = pd.read_csv("data/teamlogos.csv")
    return team_logos

def all_data():
   all_data = pd.read_csv("data/prediction_df.csv")
   return all_data

