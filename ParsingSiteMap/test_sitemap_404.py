import requests
from xml.dom import minidom

sitemap_url = 'https://staging-api.interneturok.ru/sitemap.xml'
response = requests.get(sitemap_url)
dom = minidom.parseString(response.content.decode("utf-8"))
dom.normalize()
nodes = dom.getElementsByTagName("loc")
iu_urls = [n.childNodes[0].nodeValue for n in nodes]

for n, url in enumerate(iu_urls):
    try:
        requests.get(url).raise_for_status()
    except requests.exceptions.HTTPError as e:
        print('%s ERROR: %s' % (n, e))