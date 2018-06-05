import media
import fresh_tomatoes

# movie data
antman = media.Movie("Antman 1", "some ants",
        "http://t3.gstatic.com/images?q=tbn:ANd9GcRvTs_PtoegY0eToOxODXT12cfV-AipOD6GftFO0ze7wbociMNB",  # NOQA
        "https://www.youtube.com/watch?v=4W_HuzWLLpQ") # NOQA
ironman = media.Movie("Ironman 1", "robert downey jr is the ironman",
        "https://i.annihil.us/u/prod/marvel/i/mg/c/a0/521f70fab9fd8/portrait_incredible.jpg", # NOQA
        "https://www.youtube.com/watch?v=HpX1mDEw1gk")  # NOQA
deadpool = media.Movie("Deadpool 1", "deadpool pool",
        "https://mir-s3-cdn-cf.behance.net/project_modules/2800/04eafb25626631.5634844b7293f.jpg", # NOQA
        "https://www.youtube.com/watch?v=tLmStxxzhkI") # NOQA
blackpanther = media.Movie("Black Panther", "awesome music",
        "https://vignette.wikia.nocookie.net/marvelcinematicuniverse/images/3/36/Black_Panther_Poster.jpg/revision/latest/scale-to-width-down/336?cb=20171207153752",  # NOQA
        "https://www.youtube.com/watch?v=xjDjIWPwcPU") # NOQA

# store movies in a list
movies = [antman, ironman, deadpool, blackpanther]

fresh_tomatoes.open_movies_page(movies)
