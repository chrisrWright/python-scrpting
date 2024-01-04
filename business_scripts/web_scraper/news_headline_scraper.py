import requests
from bs4 import BeautifulSoup

def scrape_espn_headlines():
    url = 'http://www.espn.com'
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = [headline.text.strip() for headline in soup.find_all('h1', class_='headline')]

        return headlines[:5]
    except Exception as e:
        print(f"Failed to fetch headlines from ESPN. Error: {e}")
        return []

def scrape_bbc_sport_headlines():
    url = 'http://www.bbc.com/sport'
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = [headline.text.strip() for headline in soup.find_all('span', class_='promo-headline')]

        return headlines[:5]
    except Exception as e:
        print(f"Failed to fetch headlines from BBC Sport. Error: {e}")
        return []

def scrape_fox_sports_headlines():
    url = 'https://www.foxsports.com'
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = [headline.text.strip() for headline in soup.find_all('h4', class_='headline')]

        return headlines[:5]
    except Exception as e:
        print(f"Failed to fetch headlines from Fox Sports. Error: {e}")
        return []

if __name__ == "__main__":
    espn_headlines = scrape_espn_headlines()
    bbc_sport_headlines = scrape_bbc_sport_headlines()
    fox_sports_headlines = scrape_fox_sports_headlines()

    # Print the headlines
    print("\nESPN Sports Headlines:")
    for index, headline in enumerate(espn_headlines, start=1):
        print(f"{index}. {headline}")

    print("\nBBC Sport Sports Headlines:")
    for index, headline in enumerate(bbc_sport_headlines, start=1):
        print(f"{index}. {headline}")

    print("\nFox Sports Sports Headlines:")
    for index, headline in enumerate(fox_sports_headlines, start=1):
        print(f"{index}. {headline}")
