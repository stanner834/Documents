import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find and extract the desired information
        # Example: Extracting all the links from the page
        links = soup.find_all('a')
        for link in links:
            print(link.get('href'))
    else:
        print("Failed to retrieve page:", response.status_code)

# Example usage
scrape_website("https://thehackernews.com/")
