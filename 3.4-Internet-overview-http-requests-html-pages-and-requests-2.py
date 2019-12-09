import requests
import re

url_input = input()
domanes = []

response = requests.get(url_input)

response.encoding = 'utf-8'
lst_urls = re.findall(r"<a(.*?)href(.*?)=(.*?)(\"|')(((.*?):\/\/)|(\.\.)|)(.*?)(\/|:|\"|')(.*)", response.text)
lst_urls.sort()

for doman in lst_urls:
    if doman[8] not in domanes:
        domanes.append(doman[8])

domanes.sort()

for i in domanes:
    print(i)
