# enter your code below
from github import Github

token = '<Your token here>'
github = Github(token)
user = github.get_user()
# user.login
repo = github.get_repo('ironhack-datalabs/madrid-oct-2018')

forks = repo.get_forks()
list_forks = list(forks)
print(list_forks)

for fork in list_forks:
    print(fork.get_languages())