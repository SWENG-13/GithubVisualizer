# imports
import streamlit as st
import datetime as dt
import plotly.graph_objects as go
from github import Github
import os

# TOKEN = os.getenv('GITHUB_TOKEN')
# g = Github(TOKEN)

# st.title("📈Github Repo Visualisation")

# user_in = None
# text_input = st.text_input("Enter Github Repository Name:", key='reponame')

    
# # def displayCommits(commit_stat):
# #     additions = {}
# #     deletions = {}
# #     for i in commit_stat:
# #         date = i["date"].strftime("%Y-%m-%d")
# #         if date in additions:
# #             additions[date] += i["additions"]
# #         else:
# #             additions[date] = i["additions"]
# #         if date in deletions:
# #             deletions[date] += i["deletions"]
# #         else:
# #             deletions[date] = i["deletions"]
# #     fig = go.Figure()
# #     fig.add_trace(go.Scatter(x = list(additions.keys()), y = list(additions.values()),
# #                     mode='lines',
# #                     name='additions'))
# #     fig.add_trace(go.Scatter(x = list(deletions.keys()), y = list(deletions.values()),
# #                     mode='lines',
# #                     name='deletions'))
# #     fig.update_layout(title='Commit Activity', autosize=False,
# #                         width=650, height=500, plot_bgcolor='#161a24')
# #     fig.update_xaxes(gridcolor='#353642')
# #     fig.update_yaxes(gridcolor='#353642')
# #     return fig

# def getRepoInfo():
#     repo = g.get_repo(st.session_state.reponame)
#     repo_stats = {
#         "name" : repo.name,
#         "stars" : repo.stargazers_count,
#         "forks" : repo.forks_count,
#         "created" : repo.created_at,
#         "owner" : repo.owner.login,
#         }
#     commits = []
#     for i in repo.get_commits():
#         if i.author.login:
#             commits_dict = {
#                 "date" : dt.strptime(i.stats.last_modified, "%a, %d %b %Y %H:%M:%S %Z"),                    "author" : i.author.login,
#                 "additions": i.stats.additions,
#                 "deletions" : i.stats.deletions
#             }
#             commits.append(commits_dict)
#         repo_stats["commits"] = len(commits)
#     i1_1, i1_2, i1_3 = st.columns([1,1,1.5]) # add optional column for avatar
    
#     with i1_1:
#         st.title(repo_stats["name"])
        
#         st.markdown("""**Created by :**\n""")
#         st.write(repo_stats["owner"])
#         st.markdown("""**Created on :**\n""")
#         st.write(repo_stats["created"].strftime("%d/%m/%Y"))
        
#     with i1_2:
#         st.markdown("""
#                     **Commits**\n
#                     """)
#         st.write(repo_stats["commits"])
#         st.markdown("""
#                     **Stars**\n
#                     """)
#         st.write(repo_stats["stars"])
#         st.markdown("""
#                     **Forks**\n
#                     """)
#         st.write(repo_stats["forks"])

#     with i1_3:
#         st.markdown("""
#                     **Contributors**\n
#                     """)
#         st.write("list of contributors")

#     i2_1, i2_2 = st.columns([1.5, 1])
#     # with i2_1:
#     #     st.markdown("""
#     #                 **Commit Activity**\n
#     #                 """)
#     #     st.plotly_chart(displayCommits(commits))
        
#     with i2_2:
#         st.markdown("""
#                     **Language Chart**\n
#                     """)
#         st.write("language pie chart here")

# if text_input:
#     getRepoInfo()
