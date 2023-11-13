import numpy as np
from pathlib import Path
import sys
import datetime as dt

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import streamlit as st

def data_prep():

  DATA = Path("../data")
  df = pd.read_csv(DATA/"small_data_team.csv")
  
  
  return fd_df
@st.cache

def team_colors():
    DATA = Path("../data")
    team_colors = pd.read_csv(DATA/"teamcolors.csv")
  
    return team_colors

