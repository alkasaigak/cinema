#GO
class CinemaParcer(object):
    def __init__(city = "msk"):
        self.city = city
    def extract_raw_content():
        self.content = requests.get('https://' + self.city + ".subcity.ru").text

