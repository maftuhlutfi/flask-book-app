
from datetime import datetime
import requests
from bs4 import BeautifulSoup

def scrap_func(links):
    results = []

    for url in links:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        title_tag = soup.find_all("h1", class_="AHFaub")[0].span
        image_tag = soup.find_all('img', class_="T75of h1kAub")[0]
        author_tag = soup.find_all("a", class_="hrTbp R8zArc")[0]
        description_tag = soup.find_all("div", jsname="bN97Pc")[0].span
        price_tag = soup.find_all("button", jsmodel="UfnShf")[0]
        rating_tag = soup.find_all("div", class_="BHMmbe")[0]
        additional_info_tag = soup.find_all("span", class_="htlgb")

        scrap_data = {
            "title": title_tag.getText(),
            "image": image_tag['src'].replace('?fife=w200-h300', ''),
            "description": description_tag.getText(),
            "author": author_tag.getText(),
            "publisher": additional_info_tag[0].getText(),
            "published_date": get_datetime(additional_info_tag[2].getText()),
            "total_pages": additional_info_tag[3].getText(),
            "isbn": additional_info_tag[4].getText(),
            "language": additional_info_tag[7].getText(),
            "genres": additional_info_tag[8].getText().split(" / "), 
            "price": float(price_tag.getText().replace(' Ebook', '').replace('$', '')),
            "link": url,
            "_id": url.split("id=")[1],
            "rating": float(rating_tag.getText())
        }

        results.append(scrap_data)

    return results

def get_datetime(d):
    list_d = d.split(" ")
    date = int(list_d[1].replace(',', ''))
    month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    month = month_list.index(list_d[0]) + 1
    year = int(list_d[2])

    return datetime(year, month, date)