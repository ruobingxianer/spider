# -*- coding: UTF-8 -*-
import requests
import sys


def getHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        fo = open("test.txt", "w")
        fo.write(r.text)
        fo.close()
        return r.text
    except:
        return "exception"


if __name__ == "__main__":
    reload(sys)
    sys.setdefaultencoding('utf8')
    url = "https://ctext.org/zh"
    print getHtmlText(url)
