#GO
import requests
class CinemaParcer(object):
    def __init__(self, city = "msk"):
        self.city = city
    def extract_raw_content(self):
        self.content = requests.get('https://' + self.city + ".subcity.ru").text

