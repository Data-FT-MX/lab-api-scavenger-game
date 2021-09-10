# enter your code below
from github import Github
from datetime import datetime, timedelta

token = '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'
github = Github(token)

repo = github.get_repo('ironhack-datalabs/madrid-oct-2018')
commits = list(repo.get_commits(since=datetime(2019,8,19) - timedelta(days=7)))
print('Num of commits made last week: ', len(commits))