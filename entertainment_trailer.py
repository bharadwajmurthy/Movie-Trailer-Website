# entertainment_trailer.py
# Creating instances of the movie class
import fresh_tomatoes
import media
ls1 = [0]

# It will create memory space for object slum_dog
ls1.append("https://www.youtube.com/watch?v=AIzbwV7on6Q")
ls1.append(".\images\\slum.jpg")
slum_dog = media.Movie("Slum dog Millionaire", "inspirational", ls1[2], ls1[1])

# It will create separate memory space for object infinity
ls1.append("https://www.youtube.com/watch?v=oXGm9Vlfx4w")
ls1.append(".\images\\infinity.jpg")
infinity = media.Movie(" Infinity", "drama", ls1[4], ls1[3])

ls1.append("www.youtube.com/watch?v=XWziSi-WN7w")
ls1.append(".\images\\garana.jpg")
garana = media.Movie("Garanamogudu", "drama ", ls1[6], ls1[5])

ls1.append(" https://www.youtube.com/watch?v=DsEAHEASW5E")
ls1.append(".\images\\atha.jpg")
atharintiki = media.Movie("Atharintiki daredhi", "A drama", ls1[8], ls1[7])

ls1.append(" https://www.youtube.com/watch?v=zw_vD_57hrE&vl=te")
ls1.append(".\images\\dhruva.jpg")
dhruva = media.Movie("Dhruva", "a sincere human being", ls1[10], ls1[9])

ls1.append("https://www.youtube.com/watch?v=oJxzTrvv-Uc")
ls1.append(".\images\\khaidhi.jpg")
khaidi = media.Movie("Khaidhino150", "A good heart person", ls1[12], ls1[11])

# Creating list of movie objects
movies = [slum_dog, infinity, garana, atharintiki, dhruva, khaidi]

# Passing the movies list to fresh_tomatoes
fresh_tomatoes.open_movies_page(movies)
