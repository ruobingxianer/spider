import requests


def getHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "exception"


if __name__ == "__name__":
    url = "https://ctext.org/zh"
    print getHtmlText(url)
