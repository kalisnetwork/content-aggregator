import requests
from bs4 import BeautifulSoup

# List of news websites to scrape
websites = [
    {
        'name': 'BBC News',
        'url': 'https://www.bbc.com/news',
    },
    {
        'name': 'CNN',
        'url': 'https://www.cnn.com',
    },
    {
        'name': 'The New York Times',
        'url': 'https://www.nytimes.com',
    },
]

def get_headlines(website):
    try:
        response = requests.get(website['url'])
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        headlines = []
        for headline in soup.find_all('h3'):
            headlines.append(headline.get_text())

        return headlines
    except Exception as e:
        print(f"Error fetching data from {website['name']}: {e}")
        return []

def main():
    print("Welcome to the Content Aggregator!")
    
    while True:
        print("\nSelect a website to fetch headlines:")
        for i, website in enumerate(websites, start=1):
            print(f"{i}. {website['name']}")
        
        choice = input("Enter the number of the website (q to quit): ").lower()
        
        if choice == 'q':
            break
        
        try:
            choice = int(choice)
            if 1 <= choice <= len(websites):
                website = websites[choice - 1]
                headlines = get_headlines(website)
                
                if headlines:
                    print(f"\nHeadlines from {website['name']}:\n")
                    for i, headline in enumerate(headlines, start=1):
                        print(f"{i}. {headline}")
                else:
                    print(f"No headlines found from {website['name']}")
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number or 'q' to quit.")

if __name__ == "__main__":
    main()
