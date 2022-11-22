# imports
import streamlit as st # web app
import streamlit.components.v1 as stc # html
import plotly.graph_objects as go # charts
from github import Github # tokens
from datetime import datetime
from collections import Counter # count

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

user_filter = False
repo_filter = False
valid = True

"Hello World"
# read token
file = open("token.txt")
token = file.read()
file.close()
git = Github(token)
 

st.title("📈Github Data Visualisation")
st.subheader="Measuring Software Engineering"

data_filter = st.selectbox("What type of data would you like to visualise?", ("", "Users", "Repository"), index=0)
if data_filter == "Users":
    user_filter = True
elif data_filter == "Repository":
    repo_filter = True
    
if user_filter == True:
    user_in = st.text_input("Enter Github Username:")
    try:
        pass # USER INPUT USERNAME AND FIND FROM API
    except Exception as e:
        st.write("User not found")
        valid = False
elif repo_filter == True:
    user_in = st.text_input("Enter Repository Link:")
    if user_in.startswith("https"):
        user_in = user_in[19:]
    if user_in.startswith("github"):
        user_in = user_in[11:]
    try:
        pass
    except Exception as e:
        st.write("Repository not found")
        valid = False
    
if user_filter == True & user_in.__eq__("vicky-emuk"): # debug
    
    i1_1, i1_2, i1_3 = st.columns(3) # add optional column for avatar 
    debug_username = "@emukperv"
    debug_name = "vic"
    debug_desc = "hi"
    debug_location = "Dublin, Ireland"

    with i1_1:
        st.markdown("""
                    **Username**\n
                    """)
        st.write(debug_username) # (user_info["name"]) e.g as a way to call user info from list
        st.markdown("""
                    **Name**\n
                    """)
        st.write(debug_name)
        st.markdown("""
                    **Description**\n
                    """)
        st.write(debug_desc)
        st.markdown("""
                    **Location**\n
                    """)
        st.write(debug_location)
        
    with i1_2:
        st.markdown("""
                    **Followers**\n
                    """)
        st.write("4") # (user_info["name"]) e.g as a way to call user info from list
        st.markdown("""
                    **Following**\n
                    """)
        st.write("2")
        
    with i1_3:
        st.markdown("""
                    **Stars Recieved**\n
                    """)
        st.write("3")
        st.markdown("""
                    **Public Repos**\n
                    """)
        st.write("2")
    
    i2_1, i2_2 = st.columns(2)
    
    with i2_1:
        st.write("""
        Followers
        """, data_filter)