import json
import requests
import base64
import time

with open ('Token.txt', 'r') as f:
    acceso=str(f.readlines()[0]).split('=')

key=acceso[0].rstrip('\n')
user=acceso[1]

repo='ironhack-datalabs/scavenger'


get_blob='http://api.github.com/repos/{}/git/trees/master?recursive=1'.format(repo)

get_blob=requests.get(get_blob, auth=(user, key))
results_blob=get_blob.json()


url_content='https://api.github.com/repos/ironhack-datalabs/scavenger/contents/'
tree=results_blob['tree']
archivos=[]
for i in range(len(tree)):
    if tree[i]['type']=='blob' and 'scavengerhunt' in tree[i]['path']:

        get_contenido=requests.get(url_content + tree[i]['path'])
        contenido=get_contenido.json()
        archivos.append((contenido['name'], contenido['content']))
        time.sleep(1)



archivos.sort()
frase=''
for texto in archivos:
    frase+=str(base64.b64decode(texto[1]))


frase=frase.replace('b\'', '').replace('\\n\'', ' ')
print('La frase buscada es: ', frase) 
