from classes.class_test_order_creation import TestOrderCreation
import pytest

class TestOrderTrack(TestOrderCreation):
    def test_order_contains_track(self):
        # """Тест на проверку, что тело ответа при создании заказа содержит track"""
        
        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha"
        }

        response = self.send_create_order_request(payload)

        error_message = (
            f"Ожидался код 201 и наличие 'track' в ответе, получены: "
            f"status code - {response.status_code}, "
            f"response json - {response.json()}"
        )
        assert response.status_code == 201 and "track" in response.json(), error_message