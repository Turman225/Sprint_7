import requests
import data as data
from settings import Base_params

class CouriersAPI(Base_params):

    def __init__(self, response):
        self.response = response

    def create_couriers(self, payloads):
        self.response = requests.post(f"{self.url}{data.create_courier_point}", data=payloads)
        return self.response

    def check_user_created(self):
        print(self.response.status_code)
        assert self.response.status_code == 201