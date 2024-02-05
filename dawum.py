import requests

class DarumTools:
    def __init__(self):
        self.DAWUM_API_URL = 'https://api.dawum.de/'
        self.rsp = requests.get(DAWUM_API_URL)

        
