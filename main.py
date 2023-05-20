'''
This code retrieves the HTML content of the IMDb webpage, extracts information about each anime series using BeautifulSoup, stores the extracted data in a DataFrame, and exports it to a CSV file.

URL: https://www.imdb.com/list/ls003753592/?sort=moviemeter,asc&st_dt=&mode=detail&page=1
'''

# Importing necessary libraries

import requests
from bs4 import BeautifulSoup
import pandas as pd


# Using try-except block to handle any exceptions that may occur during the execution of the code.
try:

    # Getting the url
    url = "https://www.imdb.com/list/ls003753592/?sort=moviemeter,asc&st_dt=&mode=detail&page=1"

    # Sending HTTP GET request to the url
    r = requests.get(url)

    # Creating BeautifulSoup object to parse the HTML content of the response using the 'html.parser'.
    soup = BeautifulSoup(r.text, 'html.parser')

    # This code will create 'my_anime_list.html' and write the html code of the website into that file with encoding UTF-8. Comment this block if you don't want to create an HTML file of this webpage
    with open('my_anime_list.html', "w", encoding='utf-8') as animeHtml:
        animeHtml.write(r.text)
        animeHtml.close()

    # Getting all 'div' tags with 'class="lister-item mode-detail"'
    animes = soup.find_all('div', class_="lister-item mode-detail")

    # Creating empty list 'animeSeries' to store the extracted information
    animeSeries = []

    for anime in animes:
        listerItemHeader = anime.find('h3', class_="lister-item-header")
        rank = listerItemHeader.span.text.strip('.')
        title = listerItemHeader.a.text
        timeSpan = listerItemHeader.find('span', class_="lister-item-year text-muted unbold").text
        categoriesClass = anime.find('p', class_="text-muted text-small")
        genre = categoriesClass.find('span', class_="genre").text.strip()
        star = anime.find('span', class_="ipl-rating-star__rating").text
        description = anime.find('p', class_="").text.strip()
        votes = anime.find('span', attrs={'name': 'nv'}).text

        animeColl = {
            "Rank": rank,
            "Title": title,
            "Duration": timeSpan,
            "Genre": genre,
            "Star": star,
            "Description": description,
            "Votes": votes,
        }

        animeSeries.append(animeColl)

    # Converting 'animeSeries' (list) into Pandas DataFrame
    animeData = pd.DataFrame(animeSeries)

    # Exporting to a 'CSV' file using 'to_csv' method and removing the index using 'index=None' argument
    animeData.to_csv('Best_anime_japanese_series_by_popularity.csv', index=None)

# Prints the exception during the execution of the code
except Exception as e:
    print(e)
