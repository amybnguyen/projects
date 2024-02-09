import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
top_movies_web_page = response.text

soup = BeautifulSoup(top_movies_web_page,"html.parser")

top_movies = [article.getText() for article in soup.find_all("h3", class_="title")]
top_movies.reverse()
print(top_movies)

with open("top_movies.txt", "w", encoding="utf-8") as file:
    for movie in top_movies:
        file.write(movie+"\n")
