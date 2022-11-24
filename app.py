# imports
import requests
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

text_input = st.text_input("Enter Github Username:", key='username')

def countStars(userDetails):
    response = requests.get(userDetails["starred_url"][:-15])
    if not response.ok:
        return "error"
    else:
        star_list = response.json()
    count = len(star_list)
    return count

def getUserInfo():
  st.session_state.user_details = dataloader.getUserInfo(st.session_state.username, token=TOKEN)
  if st.session_state.user_details["error"] == True:
    st.session_state.user_details = None
    st.write("User not found")
  else:
    i1_1, i1_2, i1_3 = st.columns([1,1,1.5]) # add optional column for avatar

    with i1_1:
        st.image(st.session_state.user_details["avatar_url"], width=200)
        st.markdown("""
                    **Followers**\n
                    """)
        st.write(st.session_state.user_details["followers"])  # (user_info["name"]) e.g as a way to call user info from list
        st.markdown("""
                    **Following**\n
                    """)
        st.write(st.session_state.user_details["following"])  # (user_info["name"]) e.g as a way to call user info from list
        st.markdown("""
                            **Star Count**\n
                            """)
        st.write(countStars(st.session_state.user_details))
    with i1_2:
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
        st.markdown("""
                    **Public Repos**\n
                    """)
        st.write(st.session_state.user_details["public_repos"])
    with i1_3:
        st.markdown("""
                    **Most Recent Repos**\n
                    """)
        st.write("list for top 5 repos")

    i2_1, i2_2 = st.columns([1.5, 1])
    with i2_1:
        st.markdown("""
                    **Recent Activity**\n
                    """)
        st.write("graph for recent activities")
    with i2_2:
        st.markdown("""
                    **Language**\n
                    """)
        st.write("pie chart for language used")

if text_input:
    getUserInfo()
