import requests

def request(url):
	try:
		return requests.get("http://" + url)
	except requests.exceptions.ConnectionError:
		pass 

target_url = "10.0.2.17/mutillidae/"

with open("/root/Downloads/subdomains-wordlist.txt", "r") as wordlist_file:
	for line in wordlist_file:
		word = line.strip()
		test_url = word+"."+target_url
		response = request(test_url)
		if response:
			print("Subdomain discovered: " + test_url)

with open("/root/Downloads/files-and-dirs-wordlist.txt", "r") as wordlist_file:
	for line in wordlist_file:
		word = line.strip()
		test_url = target_url+"/"+word
		response = request(test_url)
		if response:
			print("URL discovered: " + test_url)