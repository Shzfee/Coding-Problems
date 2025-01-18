from bs4 import BeautifulSoup
import requests

url = "https://www.nytimes.com/"
r = requests.get(url)
r_html = r.text
titles = []

soup = BeautifulSoup(r_html, features="html.parser")

for h2 in soup.find_all("h3","css-xxaj7r e1lsht870"): #where h3 is the tag and the other is the name of class
    titles.append(h2.text)

for title in titles:
    print(title)