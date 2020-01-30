import requests, sys

search = ' '.join(sys.argv[1:])
res = requests.get('http://google.com/search?q='+search)
print(res.text)