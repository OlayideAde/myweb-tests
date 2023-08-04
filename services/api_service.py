import requests 

class API:
    def __init__(self, url: str):
        self.url = url

    def request(self, http_method:str, endpoint:str):
        response = requests.request(http_method, f'{self.url}/{endpoint}')
        if response.ok:
            return response
        return None
    



    