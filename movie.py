class Movie:
    def __init__(self, title, genre, rating, year):
        self.title = title
        self.genre = genre
        self.rating = rating
        self.year = year

class MovieRecommender:
    def __init__(self):
        # Sample movie database
        self.movies = [
            Movie("The Shawshank Redemption", "Drama", 9.3, 1994),
            Movie("The Godfather", "Crime Drama", 9.2, 1972),
            Movie("Inception", "Sci-Fi", 8.8, 2010),
            Movie("The Dark Knight", "Action", 9.0, 2008),
            Movie("Pulp Fiction", "Crime Drama", 8.9, 1994),
            Movie("The Matrix", "Sci-Fi", 8.7, 1999),
            Movie("Forrest Gump", "Drama", 8.8, 1994),
            Movie("Interstellar", "Sci-Fi", 8.6, 2014),
            Movie("The Lord of the Rings", "Fantasy", 8.8, 2001),
            Movie("Avatar", "Sci-Fi", 7.8, 2009)
        ]
    
    def get_recommendations(self, preferred_genre=None, min_rating=0, max_year=2024):
        recommendations = []
        
        for movie in self.movies:
            if (preferred_genre is None or movie.genre.lower() == preferred_genre.lower()) and \
               movie.rating >= min_rating and \
               movie.year <= max_year:
                recommendations.append(movie)
        
        # Sort by rating in descending order
        recommendations.sort(key=lambda x: x.rating, reverse=True)
        return recommendations

def main():
    recommender = MovieRecommender()
    
    print("Welcome to Movie Recommender!")
    print("\nAvailable genres: Drama, Crime Drama, Sci-Fi, Action, Fantasy")
    
    while True:
        print("\nPlease enter your preferences:")
        genre = input("Preferred genre (press Enter to skip): ").strip()
        
        try:
            min_rating = float(input("Minimum rating (0-10): "))
            if not 0 <= min_rating <= 10:
                raise ValueError
        except ValueError:
            print("Invalid rating. Using default value of 0.")
            min_rating = 0
        
        try:
            max_year = int(input("Maximum year (e.g., 2024): "))
            if not 1900 <= max_year <= 2024:
                raise ValueError
        except ValueError:
            print("Invalid year. Using default value of 2024.")
            max_year = 2024
        
        recommendations = recommender.get_recommendations(genre if genre else None, min_rating, max_year)
        
        if recommendations:
            print("\nHere are your recommended movies:")
            for i, movie in enumerate(recommendations, 1):
                print(f"{i}. {movie.title} ({movie.year}) - {movie.genre} - Rating: {movie.rating}")
        else:
            print("\nNo movies found matching your criteria.")
        
        again = input("\nWould you like to get more recommendations? (yes/no): ").lower()
        if again != 'yes':
            print("Thank you for using Movie Recommender. Goodbye!")
            break

if __name__ == "__main__":
    main()
