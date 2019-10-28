#GO
import requests
'''Helps with requests'''
class CinemaParcer(object):
    '''Parces cinema sites'''
    def __init__(self, city = "msk"):
        '''Initing class'''
        self.city = city
        self.content = ""
    def extract_raw_content(self):
        '''Extracting raw content'''
        self.content = requests.get('https://' + self.city + ".subcity.ru").text
    def print_raw_content(self):
        '''Printing raw content'''
        print(self.content)

