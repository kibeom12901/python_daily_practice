from bs4 import BeautifulSoup
import requests
import lxml

response = requests.get("https://news.ycombinator.com/news")
data = response.text

soup = BeautifulSoup(data, "lxml")
print(soup.title)

title_span = soup.find_all("span", class_="titleline")
# print(title_span)
article_text = []
article_link = []

for title in title_span:
    article_text.append(title.getText())
    title_link = title.find("a")
    article_link.append(title_link.get("href"))

article_upvote = [int(score.getText().split()[0]) for score in soup.find_all("span", class_="score")]

# print(article_text)
# print(article_link)
# print(article_upvote)

highest = max(article_upvote)
highest_index = article_upvote.index(highest)

print(article_text[highest_index])
print(article_link[highest_index])


# print(title_span.find("a"))
# print(title_span.getText())

# title_link = title_span.find("a")
# print(title_link.get("href"))
# article_upvote = soup.find_all("span", class_="score").getText()
# print(f"here is {article_upvote}")


# # import lxml

# with open("website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "lxml")
# # print(soup.title)
# # print(soup.title.string)
# # print(soup.prettify())

# anchor_tags =soup.find_all(name='a')

# for tag in anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name="h1",id="name")
# print(heading)

# name = soup.select_one(selector="#name")
# print(name)
