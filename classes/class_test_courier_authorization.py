from classes.class_test_courier_creation import register_new_courier_and_return_login_password
import requests

class TestCourierAuthorization:
    def setup_method(self):
        self.base_url = "https://qa-scooter.praktikum-services.ru/api/v1/courier/login"
        # Регистрируем курьера и получаем его данные
        self.login, self.password, _ = register_new_courier_and_return_login_password()

    def send_login_request(self, payload):
        response = requests.post(self.base_url, json=payload)
        return response

    def delete_courier(self, login):
        delete_url = f"{self.base_url.replace('/login', '')}/{login}"
        response = requests.delete(delete_url)
        assert response.status_code == 200 and "ok" in response.json() and response.json()["ok"] is True, \
            f"Ожидался код 200 и 'ok': true, получен {response.status_code} и {response.json()}"

    def teardown_method(self):
        if hasattr(self, "login"):
            self.delete_courier(self.login)