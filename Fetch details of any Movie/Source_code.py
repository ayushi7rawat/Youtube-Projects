'''
Fetch details of any Movie from IMDB using Python.
Author: Ayushi Rawat
'''

#import the necessary module!                                               
from imdb import IMDb

# create an instance of the IMDb class
db = IMDb()

#1) Search for a Movie title
#store the key
key = 'spiderman'

movies = db.search_movie(key)
print(f'Searching for {key}:')

for movie in movies:
    title = movie['title']
    year = movie['year']
    print(f'{title} -- {year}')

print('---------------------------------------')
# 2) Fetch movie info
id = movies[2].getID()
movie = db.get_movie(id)

title = movie['title']
year = movie['year']
rating = movie['rating']
directors = movie['directors']
casting = movie['cast']

print('Movie info:')
print(f'{title} - {year}')
print(f'rating: {rating}')

director = ' '.join(map(str,directors))
print(f'directors: {director}')

actors = ', '.join(map(str, casting))
print(f'actors: {actors}')


print('---------------------------------------')
#3) Fetch actor info
actor_id = casting[0].getID()
person = db.get_person(actor_id)
bio = db.get_person_biography(actor_id)

name = person['name']
bdate = person['birth date']
height = person['height']
trivia = person['trivia']
titleRefs = bio['titlesRefs']

print(f'name: {name}')
print(f'birth date: {bdate}')
print(f'height: {height}')
print(f'trivia: {trivia[0]}')

titleRefs = ', '.join(map(str, titleRefs))
print(f'bio title refs: {titleRefs}')


print('---------------------------------------')
# 4) Fetch top/bottom 10 movies 
top = db.get_top250_movies()
bottom = db.get_bottom100_movies()

print('Top 10 movies are:')
for movie in top[0:9]:
	print(movie)
print()

print('Bottom 10 movies are:')
for movie in bottom[0:9]:
	print(movie)
