import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_movies():
    url = 'https://www.imdb.com/chart/top/'
    
    headers = {'User-Agent': 'Mozilla/5.0'} 
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status() # Check for HTTP errors
        
        soup = BeautifulSoup(response.text, 'html.parser')
        movie_data = []

        # Target the specific container for movies
        movies = soup.select("li.ipc-metadata-list-summary-item")
        
        for movie in movies:
            title = movie.select_one("h3.ipc-title__text").text.split('.', 1)[-1].strip() 
            
            movie_data.append({"Title": title, "Genre": "Action"}) #genre

        df = pd.DataFrame(movie_data)
        df.to_csv("movies.csv", index=False)
        print("Data scraped and saved successfully!")
        
    except Exception as e:
        print(f"Error during scraping: {e}")

if __name__ == "__main__":
    scrape_movies()





