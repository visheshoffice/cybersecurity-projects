# Web Crawler Documentation

## Introduction

This Python script is a simple web crawler designed to explore and extract links from a website. It utilizes the `requests` library to send HTTP requests and `re` (regular expressions) to parse the HTML content for links.

## Installation

This script requires Python 2.x or 3.x and the following libraries:

- `requests`
- `re`
- `urlparse` (for Python 2.x) or `urllib.parse` (for Python 3.x)

You can install these libraries using pip:

```bash
pip install requests
```

For Python 2.x:

```bash
pip install urlparse
```

For Python 3.x:

```bash
pip install urllib.parse
```

## Usage

1. Import the required libraries:

```python
import requests
import re
import urlparse  # For Python 2.x
from urllib.parse import urlparse  # For Python 3.x
```

2. Set the target URL:

```python
target_url = "http://10.0.2.17/mutillidae/"
```

3. Create an empty list to store the extracted links:

```python
target_links = []
```

4. Define the `extract_links_from` function:

```python
def extract_links_from(url):
    response = requests.get(target_url)
    return re.findall('(?:href=")(.*?)"', response.content)  # For Python 2.x
    # return re.findall('(?:href=")(.*?)"', response.content.decode(errors="ignore"))  # For Python 3.x
```

5. Define the `crawl` function:

```python
def crawl(url):
    href_links = extract_links_from(url)
    for link in href_links:
        link = urlparse.urljoin(url, link)  # For Python 2.x
        # link = urlparse.urljoin(url, link)  # For Python 3.x

        if "#" in link:
            link = link.split("#")[0]

        if target_url in link and link not in target_links:
            target_links.append(link)
            print(link)
            crawl(link)
```

6. Start crawling:

```python
crawl(target_url)
```

## Explanation

- The `extract_links_from` function retrieves the HTML content of the target URL using the `requests.get` method and extracts all the links using a regular expression.
- The `crawl` function takes a URL as input, extracts the links from it, and recursively crawls each link.
- The `crawl` function also checks for duplicate links and avoids crawling them again.
- The script is designed to handle both Python 2.x and 3.x by using the appropriate `urlparse` library.

## Conclusion

This script provides a basic framework for web crawling and can be extended to include additional functionality such as link validation, error handling, and saving the extracted links to a file.
