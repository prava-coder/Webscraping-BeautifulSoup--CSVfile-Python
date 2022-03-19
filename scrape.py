from bs4 import BeautifulSoup
#requests is used to request the webpages and get some html text
import requests
#importing csv module
from csv import writer
#creating a variable called "url" and assigning the webpage url to the variable url
url="https://www.pararius.com/apartments/amsterdam?ac=1"
#requesting the webpage to get the response
page=requests.get(url)
#creating an object soup with two parameters in BeautifulSoup
#first parameter to get the content
#second parameter to get the page in html format
soup=BeautifulSoup(page.content,"html.parser")
#creating a varibale called "lists" and in the lists we are going to the soup object to find all the sections in the
#with the class name"listing search item"
lists=soup.find_all("section",class_="listing-search-item")
with open("housing.csv","w",encoding="utf8",newline="")as f:
    thewriter=writer(f)
    header=["title","price","location","link"]
    thewriter.writerow(header)
    # creating a variable called list in the loop to find the title with a tag and a class name
    for list1 in lists:
        title = list1.find("a", class_="listing-search-item_link--title").text.replace("\n", "")
        price = list1.find("div", class_="listing-search-item__price").text.replace("\n", "")
        location = list1.find("div", class_="listing-search-item__location").text.replace("\n", "")
        link = list1.find("a", class_="listing-search-item__link").text.replace("\n", "")
        # placing all these iinformation inside an array with the name "info"
        info = [title, price, location, link]
        thewriter.writerow(info)