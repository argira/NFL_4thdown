import numpy as np
from pathlib import Path
import sys
import datetime as dt

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import streamlit as st

@st.cache
def data_prep():
  df = pd.read_csv("data/small_data_team.csv")
  return df
@st.cache

def team_colors():
    team_colors = pd.read_csv("data/teamcolors.csv")
    return team_colors

