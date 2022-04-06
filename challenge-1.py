# enter your code below
from github import Github

lab = 'ta-data-mex/lab-api-scavenger-game'

token = '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'

github = Github(token)

user = github.get_user()
user.login
print(user.login)


repo = github.get_repo(lab)
print(repo)

print(list(repo.get_forks()))

