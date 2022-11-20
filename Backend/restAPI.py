# pip -install requests

import requests
import json

# Method to request data from the api
def call_url(url, jsonName, headers, isAuth):
  if isAuth == True:
    response = requests.get(url, auth=("Kajus1331",""))
  else:
    response = requests.get(url)
  response_dict = response.json()
  with open('{}.json'.format(jsonName), 'w', encoding='utf-8') as f:
    json.dump(response_dict, f, ensure_ascii=False, indent=4)
    
# Used for testing
#matt token
token = ""
#kajus token
#token = ""     
headers = {'Authorization': 'token ' + token}
#url = 'https://api.github.com/users/HarveyBrezinaConniffe/repos'
#url = 'https://api.github.com/users/matthu2711/repos'
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
#call_url(url, "repos", headers, True)
f = open('repos.json')   # Opening JSON file
repoData = json.load(f) # returns JSON object as a dictionary
repoLength = (len(repoData))
repos = []
isRepoEmpty = []

for i in range(0, repoLength):
  repos.append(repoData[i]["name"])
  if repoData[i]["size"] > 0:
    isRepoEmpty.append(False)
  else:
    isRepoEmpty.append(True)  


# REPO FREQ

freqList = [] # Data is appended in the form [time, additions, subtractions]

for j in range(0, repoLength):
  repoName = repos[j]
  url3 = url2.format(repoName)
  listTmp = []
  if isRepoEmpty[j]:
    listTmp.append("0")
  else:
    #call_url(url3, "reposFreq", headers, True)
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
  #call_url(url, "commits", headers, True)
  f = open('commits.json')
  data = json.load(f)
  length2 = (len(data))
  commits.append(length2)
  totalCommits = totalCommits + length2

#print(totalCommits)

#----------------------- THIS IS NOT CURRENTLY WORKING DONT CHANGE!!!!!!!!------------------------------------
#-----------------------------------------------------------------------------------------------------



# CONTRIBUTORS
#url = "https://api.github.com/repos/matthu2711/{}/stats/contributors"
#url7 = "https://api.github.com/repos/matthu2711/calcWebApp/contributors"
#url5 = "https://api.github.com/repos/matthu2711/calcWebApp/stats/contributors"
#call_url(url5, "contributorStats", headers, True)

contributorsList = []   # Data is appended in the form [User, #added, #subtracted, #contributions]

for j in range(0, -1):
  print(j)
  repoName = repos[j]
  url1 = url.format(repoName)
  print(url1)
  listTmp = []
  if isRepoEmpty[j]:
    listTmp.append("null")
  elif str(repoData[j]["fork"]) == "True":
    listTmp.append("null")
  else:
    #call_url(url1, "contributorStats", headers, True)
    f = open('contributorStats.json')
    data = json.load(f)
    length2 = (len(data))
    weeks = (len(data[0]["weeks"]))
    listTmp.append(repoName)
    for i in range(0, length2):
      totalAdd = 0
      totalSub = 0
      listTmp.append(''.join(str(data[i]["author"]["login"])))
      for k in range(0, weeks):
        totalAdd = totalAdd + (data[i]["weeks"][k]["a"])
        totalSub = totalSub + (data[i]["weeks"][k]["d"])
      listTmp.append(totalAdd)
      listTmp.append(totalSub)
      listTmp.append(''.join(str(data[i]["total"])))
  contributorsList.append(listTmp)  

#print(contributorsList)  

#-------------------------------------DONT CHANGE ANYTHING ABOVE--------------------------

# Closing file
f.close()