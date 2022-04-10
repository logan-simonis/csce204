#Author: Logan Simonis
from movie import Movie

def get_movies():
    movie_list = []
    
    
    with open("assignments/assignment24/movies.txt") as file:
        for line in file:
            data = line.split(',')
            title = data[0]
            description = data[1]
            actors = data[2].split("*")
            genre = data[3].strip()
            rating = data[4].strip()
            movie_list.append(Movie(title, description, actors, genre, rating))
        return movie_list

print("**** Movie Listings ****")
while True:
    command = input("(L)ist all movies, get a movie (D)etails, or (Q)uit: ").strip().lower()
    movie_list = get_movies()
    if command == "q":
        break
    elif command == "l":
        for movie in movie_list:
            movie.display()
    elif command == "d":
        title = input("Enter Movie Name: ")
        for movie in movie_list:
            if movie.is_match(title):
                movie.display()
    else:
        print("Invalid Command")
        
print("Goodbye")