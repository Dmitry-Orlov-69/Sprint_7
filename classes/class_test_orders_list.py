import requests

class TestOrdersList:
    def setup_method(self):
        self.base_url = "https://qa-scooter.praktikum-services.ru/api/v1/orders"

    def send_get_orders_request(self, params=None):
        response = requests.get(self.base_url, params=params)
        return response