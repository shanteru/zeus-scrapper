import requests
from bs4 import BeautifulSoup

def scrape_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extracting outlet names and addresses
    articles = soup.find_all('article', class_='elementor-post')
    data = []
    for article in articles:
        name_tag = article.find('p', class_='elementor-heading-title elementor-size-default')
        if name_tag.get_text(strip=True)  != "Ingredients":
            
            name = name_tag.get_text(strip=True) 

            address_tag = name_tag.find_next('p')
            address = address_tag.get_text(strip=True) 
            data.append((name,address))
        else:
            continue

        

    # Finding the next page URL
    next_page_tag = soup.find('a', class_='page-numbers next')
    next_page_url = next_page_tag['href'] if next_page_tag else None

    return data, next_page_url

def scrape_all_pages(start_url):
    current_url = start_url
    all_data = []

    while current_url:
        data, current_url = scrape_page(current_url)
        all_data.extend(data)
    
    return all_data

