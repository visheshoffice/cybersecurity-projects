# Vulnerability Scanner

## Introduction
The Vulnerability Scanner is a Python tool designed to identify and test for potential security vulnerabilities in web applications. It uses various techniques, including crawling and form submission, to detect common vulnerabilities like Cross-Site Scripting (XSS) and SQL Injection.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/visheshoffice/vulnerability-scanner.git
   ```
2. Navigate to the `vulnerability-scanner` directory:
   ```bash
   cd 'Vulnerability Scanner'
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Import the `Scanner` class from the `scanner` module:
   ```python
   from scanner import Scanner
   ```
2. Create an instance of the `Scanner` class, providing the target URL and any links to ignore:
   ```python
   target_url = "http://example.com"
   links_to_ignore = ["http://example.com/logout"]
   scanner = Scanner(target_url, links_to_ignore)
   ```
3. Use the `crawl()` method to crawl the target website and extract links:
   ```python
   scanner.crawl()
   ```
4. Use the `run_scanner()` method to scan for vulnerabilities:
   ```python
   scanner.run_scanner()
   ```

## Examples
Here's an example of how to use the `Scanner` class to scan a website for vulnerabilities:

```python
from scanner import Scanner

target_url = "http://example.com"
links_to_ignore = ["http://example.com/logout"]
scanner = Scanner(target_url, links_to_ignore)
scanner.crawl()
scanner.run_scanner()
```

## Contributing
Contributions are welcome! If you find a bug or have a feature request, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgements
This project was inspired by [OWASP ZAP](https://www.zaproxy.org/).

## Support
For support, please contact https://www.linkedin.com/in/visheshoffice/.

## Version History
- v1.0.0 (2024-02-21): Initial release

## References
- [OWASP Top Ten](https://owasp.org/www-project-top-ten/)
- [Python Requests](https://docs.python-requests.org/en/latest/)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
