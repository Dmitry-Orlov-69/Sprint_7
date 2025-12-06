import requests

class TestOrderCreation:
    def setup_method(self):
        self.base_url = "https://qa-scooter.praktikum-services.ru/api/v1/orders"
        self.track = None

    def send_create_order_request(self, payload):
        response = requests.post(self.base_url, json=payload)
        if response.status_code == 201:
            self.track = response.json().get('track')
            print(f"Трек-номер заказа: {self.track}")  # Добавляем логирование
        return response

    def cancel_order(self):
        cancel_url = f"https://qa-scooter.praktikum-services.ru/api/v1/orders/cancel"
        response = requests.put(cancel_url, json={"track": self.track})
        assert response.status_code == 200, f"Ожидался код 200 при отмене заказа, получен {response.status_code}"
        assert response.json()["ok"] is True, "Заказ не был успешно отменён"

    def teardown_method(self):
        if self.track:
            print(f"Перед отменой заказа, трек-номер: {self.track}")  # Добавляем логирование
            self.cancel_order()
        else:
            print("Трек-номер не был установлен")