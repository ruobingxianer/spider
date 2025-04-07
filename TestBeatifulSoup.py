from bs4 import BeautifulSoup
import requests

url = "https://ctext.org/zhs"
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding

    demo = r.text
    soup = BeautifulSoup(demo, "html.parser")
    # print soup.prettify()

    print(soup.title)
    print(soup.title.string)

    print(soup.a)

    print(soup.a.attrs['href'])

    for parent in soup.a.parents:
        if parent is None:
            continue
        else:
            print(parent.name)

except:
    print("exception")
