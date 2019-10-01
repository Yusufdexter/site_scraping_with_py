import requests
from bs4 import BeautifulSoup
from csv import writer


response = requests.get("https://www.rithmschool.com/blog")
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article")

with open("blog_data.csv", "w") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["title", "link", "date", "time"])

    for article in articles:
        a_tags = article.find("a")
        title = a_tags.get_text()
        url = a_tags.attrs["href"]
        date = article.find("small").get_text()
        datetime = article.find("time").attrs["datetime"]

        csv_writer.writerow([title, url, date, datetime])