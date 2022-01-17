
from datetime import datetime
from turtle import title
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
        additional_info_tag = soup.find_all("div", class_="hAyfc")

        additional_info_data = additional_info_to_object(additional_info_tag)

        print(additional_info_data)

        scrap_data = {
            "title": title_tag.getText(),
            "image": image_tag['src'].replace('?fife=w200-h300', ''),
            "description": description_tag.getText(),
            "author": author_tag.getText(),
            "publisher": additional_info_data['Publisher'],
            "published_date": get_datetime(additional_info_data['Published on']),
            "total_pages": additional_info_data['Pages'],
            "isbn": additional_info_data['ISBN'] if 'ISBN' in additional_info_data.keys() else '',
            "language": additional_info_data['Language'],
            "genres": additional_info_data['Genres'], 
            "price": float(price_tag.getText().replace(' Ebook', '').replace('$', '').split(' ')[-1]),
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

def additional_info_to_object(infos):
    lists = []

    for info in infos:
        print(info)
        soup = BeautifulSoup(str(info), 'html.parser')
        title = soup.find('div', class_='BgcNfc').getText()

        if title == 'Genres':
            value = soup.find_all('span', class_='htlgb')
            value = list(map(map_genres, value))
            value = list(set(value))
        else:
            value = soup.find('span', class_='htlgb').getText()

        lists.append(title)
        lists.append(value)
    
    return {lists[i]: lists[i + 1] for i in range(0, len(lists), 2)}

def map_genres(genre):
    soup = BeautifulSoup(str(genre), 'html.parser')
    value = soup.find('span').getText().split(' / ')[0]

    return value