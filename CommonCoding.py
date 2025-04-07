# -*- coding: UTF-8 -*-
import requests


def getHtmlText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding

        fo = open("test.txt", "w")
        fo.write(r.text)
        fo.close()
        return r.text
    except:
        return "exception"


if __name__ == "__main__":
    url = "https://ctext.org/zhs"
    print(getHtmlText(url))
