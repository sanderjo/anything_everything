import random

movie_list = ['The Godfather', 'The Wizard of Oz', 'Citizen Kane', 'The Shawshank Redemption', 'Pulp Fiction']
movie_list = [*range(5200,5209+1)] # argument-unpacking operator
movie_list = list(range(5200,5209+1))

print(movie_list)

# pick a random element from a list of strings.
movie = random.choice(movie_list)
print(movie)
movie_list.remove(movie)

movie = random.choice(movie_list)
print(movie)
movie_list.remove(movie)

movie = random.choice(movie_list)
print(movie)
movie_list.remove(movie)

movie = random.choice(movie_list)
print(movie)
movie_list.remove(movie)

movie = random.choice(movie_list)
print(movie)
movie_list.remove(movie)

movie = random.choice(movie_list)
print(movie)
movie_list.remove(movie)

