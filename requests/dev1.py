import requests
from bs4 import BeautifulSoup

login = "http://45.79.43.178/source_carts/wordpress/wp-login.php"
url = "http://45.79.43.178/source_carts/wordpress/wp-admin"
username = 'admin'
password = '123456aA'
key = {'log':username,'pwd':password,'wp-submit':'Log in',
        'redirect_to':url,'testcokie':'1'}
res = requests.post(login,data=key)
#print(res.text)
soup = BeautifulSoup(res.text)
mydivs = soup.findAll("span",{"class":"display-name"})
print(mydivs)

