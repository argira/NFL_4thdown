import teamdecisions
#import bestdecisions
#import worstdecisions
#import topteams
import streamlit as st



OPTIONS = { "Team Decisions": teamdecisions
           #"Best Decisions": bestdecisions,
           #"Worst Decisions": worstdecisions,
           #"4th Top Performer Teams": topteams
          }

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(OPTIONS.keys()))
OPTION = OPTIONS[selection]
OPTION.app()
