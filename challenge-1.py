# enter your code below
import time

from datetime import datetime
from github import Github


#Token Generation
token= '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'
github= Github(token)
user= github.get_user()
user.login

# Challenge 1 
repo= github.get_repo('ironhack-datalabs/madrid-oct-2018')
forks= repo.get_forks()
lista_fork= list(forks)

languages_dict=[i.get_languages() for i in lista_fork] 
dict_keys=[i.keys() for i in languages_dict]
list_keys=[list(i) for i in dict_keys]
languages= set([j for i in list_keys for j in i])
print(languages)

# Challenge 2
repo = github.get_repo('ironhack-datalabs/madrid-oct-2018')
#returned commits in a paginated list
commits= list(repo.get_commits())  #es lo mismo que hacer dos pasos
commits

last_week_end= datetime.fromisoformat('2019-01-10')
last_week_start= datetime.fromisoformat('2019-10-10')

count=0
for commit in commits:
    commit_date=commit.commit.author.date
    if last_week_start>= commit_date >0last_week_end:
        count+=1
print(count)

#Challenge 3
repo= github.get_repo('ironhack-datalabs/scavenger')
contents= repo.get_contents('')

paths= []
for content in contents:
    if content.path != '.gitignore':
        folder = repo.get_contents(content.path)
        for file in folder:
            if file.path.endswith('.scavengerhunt'):
                paths.append(file.path)
        
paths.sort(key= lambda x: re.findall(r'\.\d+',x))
for path in paths:
    content= repo.get_contents(path)
    print(content.decoded_content)























