from bs4 import BeautifulSoup
import urllib, urllib.parse, urllib.request, urllib.error

url = input("Enter a URL: ")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

