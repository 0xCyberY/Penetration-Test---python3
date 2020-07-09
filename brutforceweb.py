import requests

dictionary = open('/home/kali/Desktop/dictionary.txt','r')
url = str()
url = input("please inter a URL: ")
for x in dictionary:
    req = requests.get(url + '/' + x.rstrip())
    if req.status_code == 200:
        print('The page ' + url + '/' + x + 'is available')
    #else:
        #print("The page not available")
