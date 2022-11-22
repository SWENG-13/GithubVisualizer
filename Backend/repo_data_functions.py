import os
import requests
from dotenv import load_dotenv
load_dotenv()

GITHUB_TOKEN = os.environ['GITHUB_TOKEN']


def get_repo_languages(owner: str, repo: str):
    response = requests.get(f"https://api.github.com/repos/{owner}/{repo}/languages",
        headers={'Authorization': f'access_token {GITHUB_TOKEN}'})
    
    if response.ok:
        return response.json()
    else:
        raise Exception(f'Failed to access Github API, error code: {response.status_code}')

def get_deployments_history(owner: str, repo: str):
    response = requests.get(f"https://api.github.com/repos/{owner}/{repo}/deployments",
        headers={
                'Authorization': f'access_token {GITHUB_TOKEN}',
                'Accept': 'application/vnd.github+json'
        })
    
    if response.ok:
        return response.json()
    else:
        raise Exception(f'Failed to access Github API, error code: {response.status_code}')

if __name__ == "__main__":
    test_languages = get_repo_languages("aislinggallagher", "SoftwareEngineeringAssignment2")
    print(test_languages)

    test_deployments = get_deployments_history("aislinggallagher", "SoftwareEngineeringAssignment2")
    print(test_deployments)