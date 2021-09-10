from github import Github
from operator import itemgetter

token = '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'
github = Github(token)
repo = github.get_repo('ironhack-datalabs/scavenger')

paths = []
def recursive_search(path='', paths=[]):
    for content in repo.get_contents(path):
        if content.type == 'dir':
            recursive_search(content.path, paths=paths)
        elif content.type == 'file' and content.name.endswith('.scavengerhunt'):
            paths.append((content.path, int(content.name.split('.')[1])))

recursive_search(paths=paths)
paths = [ c[0] for c in sorted(paths, key=itemgetter(1)) ]

secret = []
for p in paths:
    secret.append(repo.get_contents(p).decoded_content.decode())

print('Top Secret:')
print(' '.join(secret).replace('\n',''))