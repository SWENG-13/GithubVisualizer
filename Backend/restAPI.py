# pip -install requests

import requests;
import json;

# Used for testing
#url = 'https://api.github.com/users/HarveyBrezinaConniffe/repos'

# Create an API request
User = input("Enter the name of the user: ")

url = "https://api.github.com/users/{}/repos".format(User)

response = requests.get(url)
print("Status code: ", response.status_code)

# In a variable, save the API response.
response_dict = response.json()

with open('repos.json', 'w', encoding='utf-8') as f:
    json.dump(response_dict, f, ensure_ascii=False, indent=4)

# Opening JSON file
f = open('repos.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)

length = (len(data))

repos = []


# Iterating through the json
# list and add to a new list
for i in range(0, length):
  repos.append(data[i]["name"])

print(repos)

# Closing file
f.close()