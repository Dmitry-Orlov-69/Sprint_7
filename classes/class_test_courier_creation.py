import random
import string
import requests

# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
def register_new_courier_and_return_login_password():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    # генерируем логин, пароль и имя курьера
    login = generate_random_string(15)
    password = generate_random_string(15)
    first_name = generate_random_string(10)

    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    # возвращаем список
    return login_pass

class TestCourierCreation:
    def setup_method(self):
        self.base_url = "https://qa-scooter.praktikum-services.ru/api/v1/courier"

    def send_create_courier_request(self, payload):
        response = requests.post(self.base_url, data=payload)
        return response

    def delete_courier(self, login):
        delete_url = f"{self.base_url}/{login}"
        response = requests.delete(delete_url)
        assert response.status_code == 200 and "ok" in response.json() and response.json()["ok"] is True, \
            f"Ожидался код 200 и 'ok': true, получен {response.status_code} и {response.json()}"

    def teardown_method(self):
        if hasattr(self, "login"):
            self.delete_courier(self.login)