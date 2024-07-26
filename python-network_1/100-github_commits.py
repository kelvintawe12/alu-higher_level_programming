#!/usr/bin/env python3
"""
Fetches and lists the latest 10 commits from a GitHub repository.
Usage: ./100-github_commits.py <repo> <owner>
"""

import requests
import sys


def fetch_commits(repo, owner):
    """
    Fetches the latest 10 commits from the specified repository and owner.
    Args:
        repo (str): The name of the repository.
        owner (str): The owner of the repository.
    Returns:
        None. Prints the SHA and author name for each commit.
    """
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Error: Unable to fetch commits (status code {response.status_code})")
        return

    commits = response.json()

    for commit in commits[:10]:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")

if __name__ == "__main__" 
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repo> <owner>")
    else:
        repo = sys.argv[1]
        owner = sys.argv[2]
        fetch_commits(repo, owner)
