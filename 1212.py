import requests

url = 'http://cheb.ru'

qeuery = {'search_qeury': "кафе"}
responce = requests.get(url, params=qeuery, useragent=)

print(responce.headers, 'Heders')
print(responce.request, 'Request')
print(responce.status_code, 'Status code')