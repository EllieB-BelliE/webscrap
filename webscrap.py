import requests
from bs4 import BeautifulSoup

def main():
    webpage = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    print(webpage)
    print(webpage.url)
    soup = BeautifulSoup(webpage.content, "html.parser")
    soup_page = soup.find("p")
    print(soup_page.text)

main()

