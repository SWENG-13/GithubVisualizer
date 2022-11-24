import streamlit as st
import streamlit.components.v1 as stc
from github import Github

file = open("token.txt")
token = file.read()
file.close()
git = Github(token)
