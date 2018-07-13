# entertainment_trailer.py
# Creating instances of the movie class
import fresh_tomatoes
import media

# It will create memory space for object story_toy which has instance variables are initialized to provided arguments
slum_dog = media.Movie("Slum dog Millionaire", "A story of a boy live in slum and how he became millionaire", ".\images\\slum.jpg","https://www.youtube.com/watch?v=AIzbwV7on6Q")

# It will create separate memory space for object story_toy which has instance variables are initialized to provided arguments

infinity = media.Movie(" Infinity", "a story of great mathematician ",".\images\\infinity.jpg", "https://www.youtube.com/watch?v=oXGm9Vlfx4w")


garana = media.Movie("Garanamogudu", "a strong human being ", ".\images\\garana.jpg", "www.youtube.com/watch?v=XWziSi-WN7w")


atharintiki = media.Movie("Atharintiki daredhi", "A man went to bring his aunty back to his home", ".\images\\atha.jpg", " https://www.youtube.com/watch?v=DsEAHEASW5E")

dhruva = media.Movie("Dhruva", "a sincere human being", ".\images\\dhruva.jpg", " https://www.youtube.com/watch?v=zw_vD_57hrE&vl=te")

khaidi = media.Movie("Khaidhino150", "A good heart person", ".\images\\khaidhi.jpg", "https://www.youtube.com/watch?v=oJxzTrvv-Uc")

# Creating list of movie objects
movies = [slum_dog, infinity, garana, atharintiki, dhruva, khaidi]

# Passing the movies list to fresh_tomatoes that will display the movie trailers on web page
fresh_tomatoes.open_movies_page(movies)




