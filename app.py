import pandas as pd

def suggest_movie():
    try:
        # Load data using Pandas
        data = pd.read_csv("movies.csv")
        
        genre_input = input("Enter a movie genre (e.g., Action, Drama): ").capitalize()
        
        # Error handling for empty data or missing columns
        if data.empty:
            print("No movie data found. Please run the scraper first.")
            return
        suggestions = data[data['Genre'].str.contains(genre_input, case=False, na=False)]

        if not suggestions.empty:
            print(f"\nTop suggestions for {genre_input}:")
            print(suggestions['Title'].head(5).to_string(index=False))
        else:
            print(f"Sorry, no movies found in the '{genre_input}' genre.")

    except FileNotFoundError:
        print("Error: 'movies.csv' not found. Ensure you run the scraper script first.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    suggest_movie()