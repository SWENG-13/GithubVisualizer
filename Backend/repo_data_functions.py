import os
import requests
from dotenv import load_dotenv
from typing import List

load_dotenv()
GITHUB_TOKEN = os.environ['GITHUB_TOKEN']

def _get_repo_languages(owner: str, repo: str):
    response = requests.get(f"https://api.github.com/repos/{owner}/{repo}/languages",
        headers={'Authorization': f'access_token {GITHUB_TOKEN}'})
    
    if response.ok:
        return response.json()
    else:
        raise Exception(f'Failed to access Github API, error code: {response.status_code}')

def get_repos_languages(owners: List[str], repos: List[str]):
    languages_per_repo = {}
    for owner, repo in zip(owners, repos):
        language_stats = _get_repo_languages(owner, repo)
        languages_per_repo[f"{owner}/{repo}"] = language_stats
    
    return languages_per_repo

def _get_deployments_history(owner: str, repo: str):
    response = requests.get(f"https://api.github.com/repos/{owner}/{repo}/deployments",
        headers={
                'Authorization': f'access_token {GITHUB_TOKEN}',
                'Accept': 'application/vnd.github+json'
        })   
    if response.ok:
        return response.json()
    else:
        raise Exception(f'Failed to access Github API, error code: {response.status_code}')

def get_deployments_history_multiple_repos(owners: List[str], repos: List[str]):
    deploymets_per_repo = {}
    for owner, repo in zip(owners, repos):
        deployments_info = _get_deployments_history(owner, repo)
        deploymets_per_repo[f"{owner}/{repo}"] = deployments_info
    
    return deploymets_per_repo

if __name__ == "__main__":
    test_languages = _get_repo_languages("aislinggallagher", "SoftwareEngineeringAssignment2")
    print(test_languages)

    test_deployments = _get_deployments_history("aislinggallagher", "SoftwareEngineeringAssignment2")
    print(test_deployments)

    test_multiple_languages = get_repos_languages(
            ["aislinggallagher", "MoreeZ"], ["SoftwareEngineeringAssignment2", "sweng-2022"])
    
    print(test_multiple_languages)

    test_multiple_deployments = get_deployments_history_multiple_repos(
            ["aislinggallagher", "MoreeZ"], ["SoftwareEngineeringAssignment2", "sweng-2022"])
    
    print(test_multiple_deployments)