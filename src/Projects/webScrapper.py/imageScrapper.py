import os
import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO


def search():
    search = input("Search here: ")
    param = {"q": search}

    r = requests.get("https://www.bing.com/search", params=param)

    soup = BeautifulSoup(r.text, "html.parser")
    links = soup.findAll("a", {"class": "thumb"})

    for items in links:
        img_obj = requests.get(items.attrs["href"])
        print(img_obj)

    """
    web scrap for images and store it into Lcoal
    """


search()
