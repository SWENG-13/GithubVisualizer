# imports
import streamlit as st # web app
import streamlit.components.v1 as stc # html
import plotly.graph_objects as go # charts
from github import Github # tokens
from datetime import datetime
from collections import Counter # count
import dataloader

TOKEN = None

## function for getting and displaying profile information
    # user data: avatar (?), username, name, description, location
    # keep user data in dict or list form
    
## function for getting and displaying repo information
    # repo data:  name, star_count, languages, size
    # keep data in list form to be able to access overall repo info


st.set_page_config(
    page_title="📈Github Data Visualiser",
    page_icon="📈",
    layout="wide",
)

debug_username = "@emukperv"
debug_name = "vic"
debug_desc = "hi"
debug_location = "Dublin, Ireland"
valid = True

st.title("📈Github Data Visualisation")
st.subheader="Measuring Software Engineering"

user_in = None

st.session_state.user_details = None
def getUserInfo():
  st.session_state.user_details = dataloader.getUserInfo(st.session_state.username, token=TOKEN)
  if st.session_state.user_details["error"] == True:
    st.session_state.user_details = None
    st.write("User not found")
  else:
    i1_1, i1_2, i1_3 = st.columns(3) # add optional column for avatar 

    with i1_1:
        st.markdown("""
                    **Username**\n
                    """)
        st.write(st.session_state.username) # (user_info["name"]) e.g as a way to call user info from list
        st.markdown("""
                    **Name**\n
                    """)
        st.write(st.session_state.user_details["name"])
        st.markdown("""
                    **Description**\n
                    """)
        st.write(st.session_state.user_details["bio"])
        st.markdown("""
                    **Location**\n
                    """)
        st.write(st.session_state.user_details["location"])
        
    with i1_2:
        st.markdown("""
                    **Followers**\n
                    """)
        st.write(st.session_state.user_details["followers"]) # (user_info["name"]) e.g as a way to call user info from list
        st.markdown("""
                    **Following**\n
                    """)
        st.write(st.session_state.user_details["following"])
        
    with i1_3:
        st.markdown("""
                    **Public Repos**\n
                    """)
        st.write(st.session_state.user_details["public_repos"])

    i2_1, i2_2 = st.columns(2)

st.text_input("Enter Github Username:", key='username', on_change=getUserInfo)
