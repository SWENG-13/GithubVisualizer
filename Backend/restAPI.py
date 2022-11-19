# pip -install requests

import requests;
import json;

# Method to request data from the api
def call_url(url, jsonName, headers, isAuth):
  if isAuth == True:
    response = requests.get(url, auth=("Kajus1331","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"))
  else:
    response = requests.get(url)
  response_dict = response.json()
  with open('{}.json'.format(jsonName), 'w', encoding='utf-8') as f:
    json.dump(response_dict, f, ensure_ascii=False, indent=4)
    
# Used for testing
#matt token
token = "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"
#kajus token
#token = "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"     
headers = {'Authorization': 'token ' + token}
#url = 'https://api.github.com/users/HarveyBrezinaConniffe/repos'
url = 'https://api.github.com/users/matthu2711/repos'
url2 = 'https://api.github.com/repos/matthu2711/{}/stats/code_frequency'
#url = 'https://api.github.com/users/Kajus1331/repos'
#url2 = 'https://api.github.com/repos/Kajus1331/AlgsAssignmentFinalProject/stats/code_frequency'

# Create an API request
#isAuth = True
#user = input("Enter the name of the user: ")
#url = "https://api.github.com/users/{}/repos".format(User)
#token = input("Enter auth token for more data: ")
#if token is None:
#  isAuth = False
#else:
#  headers = {'Authorization': 'token ' + token}


# REPOS
call_url(url, "repos", headers, True)
f = open('repos.json')   # Opening JSON file
data = json.load(f) # returns JSON object as a dictionary
length = (len(data))
repos = []
isRepoEmpty = []

for i in range(0, length):
  repos.append(data[i]["name"])
  if data[i]["size"] > 0:
    isRepoEmpty.append(False)
  else:
    isRepoEmpty.append(True)  


# REPO FREQ

freqList = [] # Data is appended in the form [time, additions, subtractions]

for j in range(0, length):
  repoName = repos[j]
  url3 = url2.format(repoName)
  listTmp = []
  if isRepoEmpty[j]:
    listTmp.append("0")
  else:
    call_url(url3, "reposFreq", headers, True)
    f = open('reposFreq.json')
    data = json.load(f)
    length2 = (len(data))
    for i in range(0, length2):
      listTmp.append(''.join(str(data[i])))
  freqList.append(listTmp)    
    

# COMMITS

commits = []
totalCommits = 0

for i in repos:
  url = "https://api.github.com/repos/matthu2711/{}/commits".format(i)
  call_url(url, "commits", headers, True)
  f = open('commits.json')
  data = json.load(f)
  length = (len(data))
  commits.append(length)
  totalCommits = totalCommits + length

print(totalCommits)
# Closing file
f.close()