#!/usr/bin/python3
"""
Fetches the latest 10 commits from a GitHub.
"""

import requests
import sys
from requests.auth import HTTPBasicAuth

def fetch_commits(repo, owner):
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Error: Unable to fetch commits (status code "
              f"{response.status_code})")
        return

    commits = response.json()

    for commit in commits[:10]:
        sha = commit.get('sha', 'N/A')
        author_name = (
            commit.get('commit', {}).get('author', {}).get('name', 'Unknown')
        )
        print(f"{sha}: {author_name}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repo> <owner>")
    else:
        repo = sys.argv[1]
        owner = sys.argv[2]
        fetch_commits(repo, owner)
