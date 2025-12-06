import pytest
from classes.class_test_order_creation import TestOrderCreation

class TestOrderOneOfTheColors(TestOrderCreation):
    @pytest.mark.parametrize("color", ["BLACK", "GREY"])
    def test_order_with_one_color(self, color):
        # """Тест на проверку, что при создании заказа можно указать один из цветов — BLACK или GREY"""
        
        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": [color]
        }

        response = self.send_create_order_request(payload)

        assert response.status_code == 201, \
            f"Ожидался код 201 при создании заказа с цветом {color}, получен {response.status_code}"