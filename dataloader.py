import requests
import json

# Function that returns information about a given user
# An access token can optionally be supplied
def getUserInfo(username, token=None):
  # Add token to headers if supplied
  headers = {}
  if token is not None:
    headers["Authorization"] = "token {}".format(token)
  requestURL = 'https://api.github.com/users/{}'.format(username)
  response = requests.get(requestURL) 
  if not response.ok:
    return {"error": True, "error_details": response.json()}
  else:
    output = response.json()
    output["error"] = False
    return output

# Function that returns the names of nonempty repos of a given user
# An access token can optionally be supplied
def getRepos(username, token=None):
  # Add token to headers if supplied
  headers = {}
  if token is not None:
    headers["Authorization"] = "token {}".format(token)
  requestURL = 'https://api.github.com/users/{}/repos'.format(username)
  response = requests.get(requestURL) 
  if not response.ok:
    return {"error": True, "error_details": response.json()}
  else:
    output = {"error": False, "repo_names": []}
    data = response.json()
    # for repo in data:
    #   # Check that repo is not empty
    #   if repo["size"] > 0:
    #     output["repo_names"].append(repo["name"])
    # Return repo names
    return data
  
# Function that returns the commit frequency of each of a users repos
# Repo name must be in the format {OWNER}/{NAME}, e.g. SWENG-13/GithubVisualizer
# An access token can optionally be supplied
def getRepoFreq(username, token=None):
  repos = getRepos(username, token=None)
  # Add token to headers if supplied
  headers = {}
  if token is not None:
    headers["Authorization"] = "token {}".format(token)
  output = {"error": False, "commits": {}}
  for repo in repos["repo_names"]:
    requestURL = 'https://api.github.com/repos/{}/{}/stats/code_frequency'.format(username, repo)
    # Max number of retries
    maxRetries = 10
    # Timeout between retries
    retryTimeout = 0.1
    responseCode = 202
    attempts = 0
    while responseCode == 202 and attempts < maxRetries:
      response = requests.get(requestURL) 
      responseCode = response.status_code
      if responseCode == 202:
        continue
      if not response.ok:
        return {"error": True, "error_details": response.json()}
      else:
        commits = response.json()
        output["commits"][repo] = commits
  return output

# Function that gets the number of commits made by a user to all repos over all time
# An access token can optionally be supplied
def getTotalCommits(username, token=None):
  repos = getRepos(username, token=None)
  # Add token to headers if supplied
  headers = {}
  if token is not None:
    headers["Authorization"] = "token {}".format(token)
  output = {"error": False, "total_commits": 0}
  for repo in repos["repo_names"]:
    requestURL = "https://api.github.com/repos/{}/{}/commits".format(username, repo)
    response = requests.get(requestURL) 
    if not response.ok:
      return {"error": True, "error_details": response.json()}
    else:
      output["total_commits"] += len(response.json())
  return output

def getRepoLanguages(username, token=None):
  repos = getRepos(username, token=None)
  # Add token to headers if supplied
  headers = {}
  if token is not None:
    headers["Authorization"] = "token {}".format(token)
  output = {"error": False, "languages": {}}
  for repo in repos["repo_names"]:
    requestURL = 'https://api.github.com/repos/{}/{}/languages'.format(username, repo)
    response = requests.get(requestURL)
    if not response.ok:
      return {"error": True, "error_details": response.json()}
    else:
      data = response.json()
      for key in data.keys():
        if key in output["languages"].keys():
          output["languages"][key] += data[key]
        else:
          output["languages"][key] = data[key]
  return output

  #Function to return a list of first usernames, and secondly their corresponding contributions for the given repository
# def getTopRepoContributors(user, repo, token=None):
#   requestURL = 'https://api.github.com/repos/{username}/{repoName}/contributors'.format(username = user, repoName = repo)
#   response = requests.get(requestURL)
#   data = response.text
#   r = json.loads(data)
#   contributorDict = dict()
#   contributorList = []
#   for i in r:
#     username = i['login']
#     contributions = i['contributions']
#     contributorDict[username] = contributions
#   sort = sorted(contributorDict.items(), key=lambda item:  item[1], reverse = True)

#   result = []
#   if(len(sort) >= 5): 
#     for i in range(0,5):
#         result.append(sort[i])
#   else:
#     result = sort

#   usernames = []
#   conts = []
#   for i in result:
#     usernames.append(i[0])
#     conts.append(i[1])  

#   output = []
#   output.append(usernames)
#   output.append(conts)
#   return output


"""
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
    """
