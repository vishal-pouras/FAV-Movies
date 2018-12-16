import media,to_html

toy_story = media.Movie("Toy Story",
                        "A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=P9-jf9-c9JM")

print(toy_story.storyline)
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
print(avatar.title)
#avatar.show_trailer()

the_shawshank_redemption = media.Movie("The Shawshank Redemption",
                                       "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
                                        "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                                        "https://www.youtube.com/watch?v=6hB3S9bIaco")
#the_shawshank_redemption.show_trailer()

django_unchained = media.Movie("Django Unchained",
                          "With the help of a German bounty hunter, a freed slave sets out to rescue his wife from a brutal Mississippi plantation owner.",
                          "https://upload.wikimedia.org/wikipedia/en/8/8b/Django_Unchained_Poster.jpg",
                          "https://www.youtube.com/watch?v=eUdM9vrCbow")

shutter_island = media.Movie("Shutter Island",
                            "In 1954, a U.S. Marshal investigates the disappearance of a murderer, who escaped from a hospital for the criminally insane.",
                            "https://upload.wikimedia.org/wikipedia/en/7/76/Shutterislandposter.jpg",
                            "https://www.youtube.com/watch?v=YDGldPitxic")

inception = media.Movie("Inception",
                        "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO.",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=d3A3-zSOBT4")

movies = [toy_story,avatar,the_shawshank_redemption,django_unchained,shutter_island,inception]
to_html.open_movies_page(movies)