from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import re
import time

def scrape_emails_selenium(url):
    # Path to chromedriver
    path_to_chromedriver = 'chromedriver.exe' # Replace with your chromedriver path

    # Setup the webdriver options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')  # Run Chrome in headless mode (optional)
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    # Initialize the Chrome WebDriver with the specified options and path
    service = Service(executable_path=path_to_chromedriver)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Open the webpage
    driver.get(url)

    # Wait for the page to load
    time.sleep(5) # Adjust the sleep time as necessary

    # Get the page source
    html = driver.page_source
    driver.quit()

    # Parse the webpage content
    soup = BeautifulSoup(html, 'html.parser')

    # Regular expression pattern for finding emails
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

    # Find all emails in the webpage
    emails = set(re.findall(email_pattern, soup.get_text()))

    return list(emails)

# URL of the website to scrape
url = 'https://www.myams.org/clubs/club-directory/'

# Scrape emails and print them
emails = scrape_emails_selenium(url)
for email in emails:
    print(email)
