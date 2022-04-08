#Author: Logan Simonis
from movie import Movie

movieList = (
    Movie("No Time to Die", "James Bond has lef active service", ["Daniel Craig", "Ana de Armas", "Rami Malek"], "Thriller", 7.4),
    Movie("The Last Letter from Your Lover", "A pair of interwoven stories set in the past and present", ["Shailene Woodley", "Joe Alwyn", "Wendy Nottingham"], "Romance", 6.7),
    Movie("Passing", "Passing, follows the unexpected reunion of two high school friends", ["Tessa Thompson", "Ruth Negga", "Andre Holland"], "Drama", 6.6),
    Movie("Last Night in Soho", "An aspiring fashion designer is mysteriously able to enter the 1960s", ["Thomasin Mckenzie", "Anya Taylor-Joy", "Matt Smith"], "Mystery", 7.2)   
)
print("**** Movie Listings ****")
while True:
    command = input("(L)ist all movies, get a movie (D)etails, or (Q)uit: ").strip().lower()
    
    if command == "q":
        break
    elif command == "l":
        for movie in movieList:
            movie.display()
    elif command == "d":
        title = input("Enter Movie Name: ")
        for movie in movieList:
            if movie.is_match(title):
                movie.display()
    else:
        print("Invalid Command")
        
print("Goodbye")