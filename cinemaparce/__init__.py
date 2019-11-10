import requests
from bs4 import BeautifulSoup
'''Helpfull moduls'''

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
        if (self.content == None):
            self.extract_raw_content()
        print(self.content.text)
    
    def get_film_list(self):
        '''Finding actual films'''
        if (self.content == None):
            self.extract_raw_content()
        text = BeautifulSoup(self.content.text, features='html.parser')
        unparsed_films = text.find_all('div', {'class': 'movie-title'})
        ans = []
        for film in unparsed_films:
            try:
                film.text.replace('\xad', '')
                film.text.replace('\xa0', '')
                ans.append(film.text.split(' (')[0])
            except:
                pass
        return ans
    
    def get_film_page(self, name):
        '''Finding a page of the film'''
        if (self.content == None):
            self.extract_raw_content()
        film_items = BeautifulSoup(self.content.text, features='html.parser').find_all('div', {'class': 'movie-plate', 'attr-title': name})
        for item in film_items:
            ans = str(item)[str(item).find('http://m.kinopoisk.ru/movie/'):].split('"')[0]
            if (len(ans) != 0):
                return ans;
        return None
    
    def get_film_nearest_session(self, name):
        '''Finding film nearest session'''
        if (self.content == None):
            self.extract_raw_content()
        page = self.get_film_page(name)
        content = requests.get(page)
        link = (page + content.text[content.text.find('afisha/city/'):].split('"')[0])
        content = requests.get(link).text
        cinema = content[content.find('schedule-cinema__name') + 22:].split('<')[0]
        time = content[content.find('schedule-item__template') + 25:].split('<')[0]
        return cinema, time


p = CinemaParser()
p.extract_raw_content()
p.print_raw_content()
print(p.get_film_nearest_session("Джокер"))
