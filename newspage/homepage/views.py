from bs4 import BeautifulSoup
import requests
from django.http import HttpResponse
from django.shortcuts import render
from datetime import date

datums = date.today()

#Vardadienas
def vardadienas():

    page = requests.get('https://www.1188.lv/varda-dienas')
    soup = BeautifulSoup(page.text, 'html.parser')

    elements = soup.find(class_='names').text

    return elements

#Delfi
def delfi():

    page = requests.get('https://www.delfi.lv/')
    soup = BeautifulSoup(page.text, 'html.parser')

    elements = soup.find_all(class_="text-size-16 text-size-md-19 d-block", limit=6)

    out = []
        
    for item in elements:
        title = item.find("h1").text.strip()
        link = item.find("a", href=True)

        if 'PLUS' in title:
            title = title.split('PLUS')[1]

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

        if title[-1] == ')':
            title = title[:-4]
        
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

        if title[-1] == ')':
            title = title[:-4]
        
        out.append([title,link])

    return out

#La
def la():

    la = requests.get('https://www.la.lv')
    soup = BeautifulSoup(la.text, 'html.parser')

    elements = soup.find_all(class_='content-item lazy-load', limit=6)

    out = []

    for item in elements:
        title = item.find(class_='ci-title').text.split('\n')[1].strip()
        link = item['href']

        out.append([title,link])

    return out

#BBC
def bbc():

    bbc = requests.get('https://www.bbc.com/')
    soup = BeautifulSoup(bbc.text, 'html.parser')

    elements = soup.find_all(class_='block-link', limit=6)

    out = []

    for item in elements:
        title = item['data-bbc-title'].strip()
        link = item.find(class_='block-link__overlay-link')['href']

        if link[0] == '/':
            link = 'https://www.bbc.com' + link
            
        out.append([title,link])

    return out

#Nbcnews
def nbcnews():

    nbcnews = requests.get('https://www.nbcnews.com/')
    soup = BeautifulSoup(nbcnews.text, 'html.parser')

    elements = soup.find_all(class_='tease-card__headline tease-card__title relative', limit=6)

    out = []

    for item in elements:
        title = item.find(class_='tease-card__headline').text.strip()
        link = item.find('a')['href']
            
        out.append([title,link])

    return out

#Theguardian
def theguardian():

    theguardian = requests.get('https://www.theguardian.com/world')
    soup = BeautifulSoup(theguardian.text, 'html.parser')

    elements = soup.find_all(class_='u-faux-block-link__overlay js-headline-text', limit=6)

    out = []

    for item in elements:
        title = item.text.strip()
        link = item['href']
            
        out.append([title,link])

    return out

#Nytimes
def nytimes():

    nytimes = requests.get('https://www.nytimes.com/section/world')
    soup = BeautifulSoup(nytimes.text, 'html.parser')

    elements = soup.find_all(class_='css-qrzo5d e134j7ei0', limit=6)

    out = []

    for item in elements:
        title = item.text.strip()
        link = item.find('a')['href']
            
        out.append([title,link])

    return out


# Create your views here.

def home_view(request, *args, **kwargs):

    thing = {
            'datums' : datums,
            'vardadienas' : vardadienas(),
            'delfi' : delfi(),
            'apollo' : apollo(),
            'tvnet' : tvnet(),
            'la' : la(),
            'bbc' : bbc(),
            'nbcnews' : nbcnews(),
            'theguardian' : theguardian(),
            'nytimes' : nytimes()
            }

    return render(request, "homepage.html", thing)