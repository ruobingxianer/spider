import requests

r = requests.get("https://ctext.org/zhs")

print (r.status_code)

r.encoding = "utf-8"

print (r.text)