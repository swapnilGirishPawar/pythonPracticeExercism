from bs4 import BeautifulSoup
import requests


def line():
    print("_____________________________________________________________________")


search = input("Enter search here : ")
param = {"q": search}
r = requests.get("https://www.bing.com/search", params=param)

soup = BeautifulSoup(r.text, "html.parser")
results = soup.find("ol", {"id": "b_results"})
links = results.find_all("li", {"class": "b_algo"})
for items in links:
    item_text = items.find("a").text
    item_href = items.find("a").attrs["href"]

    if item_text and item_href:
        line()
        print("Text : ", item_text)
        print("Href : ", item_href)

        print("parent : ", items.find("a").parent.parent.find("p").text)
        children = items.children[0]

        for child in children:
            print("Child : ", child)

        line()

print("page ends here")
