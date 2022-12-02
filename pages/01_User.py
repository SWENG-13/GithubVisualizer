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
import json


TOKEN = None
g = Github(TOKEN)
# debug_username = 'DavyOLearyF'

st.title("📈Github User Visualisation")

user_in = None

st.session_state.user_details = None
st.session_state.language_data = None

text_input = st.text_input("⬇️Enter Github Username:", key='username')

#Davys Code -------------------------------

# def sortable_date(x):
#     d,t = x['Last Updated'].split('T')
#     dtoks = d.split('-')
#     #        year     month    day     time
#     return (dtoks[0],dtoks[1],dtoks[2],t)

# reposDict = dict()
# repoList = []

# file = dataloader.getRepos(debug_username, TOKEN) 

# for i in file:
#     repoName = i['name']
#     lastUpdated = i['updated_at']
#     reposDict[repoName] = lastUpdated
#     x={
#     "Repository Name": repoName,
#     "Last Updated": lastUpdated
#     }
#     repoList.append(x)


# reposResult = sorted(repoList,key=sortable_date, reverse=True)

# repoNames = []
# recentDates = []
# for i in range(0,5):
#     repoNames.append(reposResult[i]["Repository Name"])
#     tmp, tmp2 = reposResult[i]["Last Updated"].split('T')
#     recentDates.append(tmp)

#-----------------------------------------------

def countStars(userDetails):
    response = requests.get(userDetails["starred_url"][:-15])
    if not response.ok:
        return "error"
    else:
        star_list = response.json()
    count = len(star_list)
    return count

def languageAnalyse(lanDetails):
    key_arr = []
    val_arr = []
    for key in lanDetails["languages"].keys():
        key_arr.append(key)
    for value in lanDetails["languages"].values():
        val_arr.append(value)
    df = pd.DataFrame({"language": key_arr, "size": val_arr})
    pieChart = px.pie(df, names="language", values="size", title="🗣️Languages")
    return pieChart
    
def displayActivity(activity):
    activity_count = dict(Counter(activity))
    keys = list(activity_count.keys())
    values = list(activity_count.values())
    fig = go.Figure(data=[go.Scatter(x=keys, y = values)])
    fig.update_layout(title='💻Recent Activity:', autosize=False,
                        width=650, height=500, plot_bgcolor='#161a24')
    fig.update_xaxes(gridcolor='#353642')
    fig.update_yaxes(gridcolor='#353642')
    return fig

def getUserInfo():
    usr = g.get_user(st.session_state.username)
    st.session_state.user_details = dataloader.getUserInfo(
        st.session_state.username, token=TOKEN)
    st.session_state.language_data = dataloader.getRepoLanguages(
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
                    **📛Username**\n
                    """)
        st.write(st.session_state.username) # (user_info["name"]) e.g as a way to call user info from list
        st.markdown("""
                    **😊Name**\n
                    """)
        st.write(st.session_state.user_details["name"])
        st.markdown("""
                    **📋Description**\n
                    """)
        st.write(st.session_state.user_details["bio"])
        st.markdown("""
                    **Location**\n
                    """)
        st.write(st.session_state.user_details["location"])
    with i1_2:
        st.markdown("""
                    **👣Followers**\n
                    """)
        st.write(st.session_state.user_details["followers"])  # (user_info["name"]) e.g as a way to call user info from list
        st.markdown("""
                    **👣Following**\n
                    """)
        st.write(st.session_state.user_details["following"])  # (user_info["name"]) e.g as a way to call user info from list
        st.markdown("""
                    **🌟Star Count**\n
                    """)
        st.write(countStars(st.session_state.user_details))
        st.markdown("""
                    **👀Public Repos**\n
                    """)
        st.write(st.session_state.user_details["public_repos"])
    with i1_3:
        st.markdown("""
                    **Most Recent Repos**\n
                    """)
        st.write("list for top 5 repos")

        # st.write(pd.DataFrame({
        #     'Repo Name': repoNames,
        #     'Last Updated': recentDates
        #     }))

    i2_1, i2_2 = st.columns([1.5, 1])
    with i2_1:
        st.plotly_chart(displayActivity(user_activity))
        
    with i2_2:
        st.plotly_chart(languageAnalyse(st.session_state.language_data))

if text_input:
    getUserInfo()
