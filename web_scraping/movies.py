from bs4 import BeautifulSoup
import requests
import lxml

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
data = response.text

soup = BeautifulSoup(data, "lxml")

titles = soup.find_all(name = "h3", class_="title")

movie_titles = [title.getText() for title in titles]
movies_ordered = []
for n in range(len(movie_titles)-1,-1,-1):
    movies_ordered.append(movie_titles[n])

# print(movie_titles[::-1])

with open("movies.txt", mode="w") as file:
    for movie in movies_ordered:
        file.write(f"{movie}\n")
        
