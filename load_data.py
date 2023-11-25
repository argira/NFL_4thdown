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
  df = pd.read_csv("data/small_data_team.csv")
  return df
@st.cache_data
def data_prep_new():
  df = pd.read_csv("data/new_data_team.csv")
  return df
@st.cache_data

def team_colors():
    team_colors = pd.read_csv("data/teamcolors.csv")
    return team_colors

@st.cache_data

def team_logos():
    team_logos = pd.read_csv("data/teamlogos.csv")
    return team_logos

def all_data():
   all_data = pd.read_csv("data/all_data.csv")
   return all_data

