# imports
from collections import Counter
import requests
import dataloader
import streamlit as st
import datetime as dt
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from github import Github

TOKEN = "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"
g = Github(TOKEN)
# function for getting and displaying profile information
    # user data: avatar (?), username, name, description, location
    # keep user data in dict or list form

# function for getting and displaying repo information
    # repo data:  name, star_count, languages, size
    # keep data in list form to be able to access overall repo info


st.set_page_config(
    page_title="Github Data Visualiser",
    page_icon="📈",
    layout="wide",
)

st.title("📈Github Data Visualisation")
st.subheader = "Measuring Software Engineering"

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

def displayActivity(activity):
    activity_count = dict(Counter(activity))
    keys = list(activity_count.keys())
    values = list(activity_count.values())
    fig = go.Figure(data=[go.Scatter(x=keys, y = values)])
    fig.update_layout(title='Recent Activity:', autosize=False,
                        width=650, height=500, plot_bgcolor='#161a24')
    fig.update_xaxes(gridcolor='#353642')
    fig.update_yaxes(gridcolor='#353642')
    return fig

def getUserInfo():
    usr = g.get_user(st.session_state.username)
    st.session_state.user_details = dataloader.getUserInfo(
        st.session_state.username, token=TOKEN)
    if st.session_state.user_details["error"] == True:
        st.session_state.user_details = None
        st.write("User not found")
    else:
        i1_1, i1_2, i1_3 = st.columns([1,1,1.5]) # add optional column for avatar
        user_activity = []
        for i in usr.get_events():
            date = i.created_at.date()
            date = date.strftime("%Y-%m-%d")
            user_activity.append(date)

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
        st.plotly_chart(displayActivity(user_activity))
        
    with i2_2:
        st.markdown("""
                    **Language**\n
                    """)
        st.write("pie chart for language used")

if text_input:
    getUserInfo()