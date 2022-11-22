# pip -install requests

import requests
import json

repoLength = 0
repos = []
isRepoEmpty = []
freqList = [] # Data is appended in the form [time, additions, subtractions]
commits = []
totalCommits = 0
repoData = []
contributorsList = []   # Data is appended in the form [User, #added, #subtracted, #contributions]
userInfoList = []
loadUser = []
userData = []


# Method to request data from the api
def call_url(url, jsonName, headers, isAuth):
  if isAuth == True:
    response = requests.get(url, headers = headers)
  else:
    response = requests.get(url)
  response_dict = response.json()
  with open('{}.json'.format(jsonName), 'w', encoding='utf-8') as f:
    json.dump(response_dict, f, ensure_ascii=False, indent=4)

def getUserInfo(headers, url):
  global loadUser, userData
  call_url(url, "user", headers, True)
  f = open('user.json')
  loadUser = json.load(f)
  userData.append(''.join(str(loadUser["login"])))
  userData.append(''.join(str(loadUser["followers"])))
  userData.append(''.join(str(loadUser["name"])))
  userData.append(''.join(str(loadUser["following"])))
  userData.append(''.join(str(loadUser["public_repos"])))
  userData.append(''.join(str(loadUser["bio"])))
  userData.append(''.join(str(loadUser["location"])))
  userData.append(''.join(str(loadUser["avatar_url"])))
  print(userData)



def getRepos(headers, url):
  global repos, repoLength, repoData, isRepoEmpty
  call_url(url, "repos", headers, True)
  f = open('repos.json')   # Opening JSON file
  repoData = json.load(f) # returns JSON object as a dictionary
  repoLength = (len(repoData))
  for i in range(0, repoLength):
    repos.append(repoData[i]["name"])
    if repoData[i]["size"] > 0:
      isRepoEmpty.append(False)
    else:
      isRepoEmpty.append(True)  

def getRepoFreq(headers, url2):
  global freqList
  for j in range(0, repoLength):
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

def getCommits(headers):
  global commits, totalCommits
  for i in repos:
    url = "https://api.github.com/repos/matthu2711/{}/commits".format(i)
    call_url(url, "commits", headers, True)
    f = open('commits.json')
    data = json.load(f)
    length2 = (len(data))
    commits.append(length2)
    totalCommits = totalCommits + length2

def getContributorData(headers, url):
  global contributorsList
  print(repoLength)
  for j in range(0, repoLength):
    repoName = repos[j]
    url1 = url.format(repoName)
    listTmp = []
    if isRepoEmpty[j]:
      listTmp.append("null")
    elif str(repoData[j]["fork"]) == "True":
      listTmp.append("null")
    else:
      call_url(url1, "contributorStats", headers, True)
      f = open('contributorStats.json')
      data = json.load(f)
      while (len(data)) == 0 :
        print("here")
        call_url(url1, "contributorStats", headers, True)
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

    
# Used for testing/ ----------------CHANGE THEM WHEN TESTING
token = "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"     
headers = {'Authorization': 'token ' + token}
urlUser = 'https://api.github.com/users/matthu2711'
urlRepo = 'https://api.github.com/users/matthu2711/repos'
urlFreq = 'https://api.github.com/repos/matthu2711/{}/stats/code_frequency'
urlContr = 'https://api.github.com/repos/matthu2711/{}/stats/contributors'

# Create an API request
#isAuth = True
#user = input("Enter the name of the user: ")
#url = "https://api.github.com/users/{}/repos".format(User)
#token = input("Enter auth token for more data: ")
#if token is None:
#  isAuth = False
#else:
#  headers = {'Authorization': 'token ' + token}


# GET USER INFO
#getUserInfo(headers, urlUser)

# GET REPOS
getRepos(headers, urlRepo)
#print(repos)
#print(repoLength)

# REPO FREQ
#getRepoFreq(headers, urlFreq)
#print(freqList)
#print(repoData)

# COMMITS
#getCommits(headers)
#print(totalCommits)

# CONTRIBUTORS
getContributorData(headers, urlContr)
print(contributorsList)