# enter your code below
from github import Github
from datetime import datetime, timedelta

token = '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'
github = Github(token)

repo = github.get_repo('ironhack-datalabs/madrid-oct-2018')
langs = []

for fork in repo.get_forks():
    langs += list(fork.get_languages().keys())
langs = set(langs)
print('languages used: ', langs)