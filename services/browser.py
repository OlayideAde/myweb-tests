class Browser:
    def __init__(self, url: str):
        self.url = url
        
    def find_object(self, object_name: str):
        # TODO: return the specified object of the website DOM