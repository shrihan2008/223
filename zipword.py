import time
import zipfile

folderpath=input("Enter path to folder")
zipf=zipfile.ZipFile(folderpath)
global result
global tried

result=0
tried=0

c=0

if not zipf:
    print("succesfully opened folder")

else:
    startime=time.time()
    wordslistfile=open("f.txt","r")
    body=wordslistfile.lower()
    words=body.split('\n')

for i in range (len(words)):
    word=words[i]
    pwd=word.encode('utf8').strip()
    c+=1
    try:
        with zipfile.ZipFile(folderpath,'r') as zf:
            zf.extractall(pwd=pwd)

            endtime=time.time()
            result=1
            break
    except:
            pass

if(result==0):
     print("not cracked")

else:
     print("cracked")
    





