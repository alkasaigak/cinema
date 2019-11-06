'''Helpfull'''
import requests
from bs4 import BeautifulSoup

class CinemaParser:
    '''Class. Parces cinema sites'''
    def __init__(self, city='msk'):
        '''Initing class'''
        self.city = city
        self.content = None
    def extract_raw_content(self):
        '''Extracting raw content'''
        self.content = requests.get('https://' + self.city + '.subscity.ru')
    def print_raw_content(self):
        '''Printing raw content'''
        print(self.content.text)
    def get_film_list(self):
        '''Finding actual films'''
        text = BeautifulSoup(self.content.text, features='lxml')
        unparsed_films = text.find_all('div', {'class': 'movie-title'})
        ans = []
        for film in unparsed_films:
            try:
                film.text.replace('\xad', '')
                film.text.replace('\xa0', '')
                ans.append(film.text.split(' (')[0])
            except TypeError:
                pass
        return ans
    def get_film_page(self, name):
        '''Finding a page of the film'''
        tmp = BeautifulSoup(self.content.text, features='lxml')
        film_items = tmp.find_all('div', {'class': 'movie-plate', 'attr-title': name})
        for item in film_items:
            ans = str(item)[str(item).find('http://m.kinopoisk.ru/movie/'):].split('"')[0]
            if ans != '':
                return ans
        return None
    def get_film_nearest_session(self, name):
        '''Finding film nearest session'''
        page = self.get_film_page(name)
        content = requests.get(page)
        link = (page + content.text[content.text.find('afisha/city/'):].split('"')[0])
        content = requests.get(link)
        cinema = content.text[content.text.find("class= ' '") + 10:].split('<')[0]
        return cinema
