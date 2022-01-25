import requests
import csv 
from keys import api_key

# include: Movie Title (string)
# Runtime (integer)
# Genre (string)
# Award Wins (integer)
# Award Nominations (integer) - part of awards, will need to be separated out later 
# Box Office (integer)

imdb_ids = []
with open("oscar_winners.csv") as csvfile:
    data = csv.reader(csvfile)
    next(data)
    for row in data: 
        imdb_ids.append(row[1])


f = open('movies.csv', 'w', newline="") 
writer = csv.writer(f)
header = ['Title', 'Runtime', 'Genre', 'Awards', 'Box_office']
writer.writerow(header)


for id in imdb_ids:
    res = requests.get(f"http://www.omdbapi.com/?apikey={api_key}&i={id}")
    raw_mov = res.json()
    Title = raw_mov['Title']
    Runtime = raw_mov['Runtime']
    Genre = raw_mov['Genre']
    Awards = raw_mov['Awards']  
    Box_office = raw_mov['BoxOffice']

    writer.writerow([Title, Runtime, Genre, Awards, Box_office])



