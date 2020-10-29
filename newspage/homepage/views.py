from bs4 import BeautifulSoup
import requests
from django.http import HttpResponse
from django.shortcuts import render


#Delfi
def delfi():

    page = requests.get('https://www.delfi.lv/')
    soup = BeautifulSoup(page.text, 'html.parser')

    element1 = soup.find_all(class_="text-size-16 text-size-md-19 d-block", limit=6)

    out = []
        
    for item in element1:
        title = item.find("h1").text.strip()
        link = item.find("a", href=True)
        out.append([title,link["href"]])

    return out


#Apollo
def apollo():

    apollo = requests.get('https://www.apollo.lv')
    soup = BeautifulSoup(apollo.text, 'html.parser')

    elements = soup.find_all(class_='list-article__url', limit=6)

    out = []

    for item in elements:
        title = item.find('span').text.strip()
        link = item['href']
        
        out.append([title,link])

    return out 


#Tvnet
def tvnet():

    tvnet = requests.get('https://www.tvnet.lv')
    soup = BeautifulSoup(tvnet.text, 'html.parser')

    elements = soup.find_all(class_='list-article__url', limit=6)

    out = []

    for item in elements:
        title = item.find('span').text.strip()
        link = item['href']
        
        out.append([title,link])

    return out


# Create your views here.

def home_view(request, *args, **kwargs):

    thing = {
            'delfi' : delfi(),
            'apollo' : apollo(),
            'tvnet' : tvnet()
            }

    return render(request, "homepage.html", thing)