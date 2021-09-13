# enter your code below

import time
from github import Github


github = Github(token)

repo = github.get_repo('ironhack-datalabs/madrid-oct-2018')

t = repo.get_forks()
print(list(t))

for a in list(t):
    f = list(a.get_languages().keys())
    print(f)
    
from datetime import datetime, timedelta

p = repo.get_commits(since=(datetime(2019,8,19) - timedelta(days=7)))
commits = list(p)
print(commits)

len(commits)

paths=[]
def recursive_search(path='', paths=[]):
    for content in repo.get_contents(path):
        if content.type == 'dir':
            recursive_search(content.path, paths=paths)
        elif content.type == 'file' and content.name.endswith('.scavengerhunt'):
            paths.append((content.path, int(content.name.split('.')[1])))
            
recursive_search(paths=paths)

print(paths)

lst_sorted = sorted(paths, key=lambda tup: tup[1])

print(lst_sorted)

path_lst = []
for i in range(len(lst_sorted)):
    path_lst.append(lst_sorted[i][0])
                    
print(path_lst)

for j in path_lst:
    print(repo.get_contents(j).decoded_content.decode())


