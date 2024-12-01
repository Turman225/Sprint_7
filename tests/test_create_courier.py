from models.couriers_model import CouriersAPI
import requests
import data

class TestCreateCourier:

    response = requests
    def test_create_courier(self):
        create_courier_model = CouriersAPI(self.response)
        create_courier_model.create_couriers(data.create_user_payload)
        create_courier_model.check_user_created()