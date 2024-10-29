import requests
from bs4 import BeautifulSoup
import pandas as pd

class WebScraper:
    def __init__(self):
        self.data = []

    def scrape_data(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        for item in soup.find_all('h2'):
            self.data.append(item.get_text())
        print(f"Scraped {len(self.data)} headlines from {url}")

    def save_to_csv(self, filename='scraped_data.csv'):
        df = pd.DataFrame(self.data, columns=['Headlines'])
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")

# Example usage
scraper = WebScraper()
url = input("Enter the URL to scrape: ")
scraper.scrape_data(url)
scraper.save_to_csv()
