import requests
import re
import urlparse #pip3 install urllib.parse for python3 and change urlparse to urllib.parse

target_url = "http://10.0.2.17/mutillidae/"
target_links = []

def extarct_links_from(url):	
	response = requests.get(target_url)
	return re.findall('(?:href=")(.*?)"', response.content) #do str(response.content) OR response.content.decode(errors="ignore") for python3

def crawl(url):
	href_links = extarct_links_from(url)
	for link in href_links:
		link = urlparse.urljoin(url, link)

		if "#" in link:
			link = link.split("#")[0]

		if target_url in link and link not in target_links:
			target_links.append(link)
			print(link)
			crawl(link)

crawl(target_url)