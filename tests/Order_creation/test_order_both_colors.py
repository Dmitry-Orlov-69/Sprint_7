from classes.class_test_order_creation import TestOrderCreation
import pytest

class TestOrderBothColors(TestOrderCreation):
    def test_order_with_both_colors(self):
        # """Тест на проверку, что при создании заказа можно указать оба цвета — BLACK и GREY"""
        
        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": ["BLACK", "GREY"]
        }

        response = self.send_create_order_request(payload)

        assert response.status_code == 201, \
            f"Ожидался код 201 при создании заказа с цветами BLACK и GREY, получен {response.status_code}"