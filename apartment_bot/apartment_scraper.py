from pprint import pprint
import requests
from bs4 import BeautifulSoup

URL = "https://www.immonet.de/immobiliensuche/sel.do?&sortby=0&suchart=1&objecttype=1&marketingtype=2&parentcat=1&toprice=900&fromrooms=2&city=87372&locationname=Berlin"
page = requests.get(URL, timeout=100)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find_all("p")

pprint(results)
