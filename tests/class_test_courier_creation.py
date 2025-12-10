import pytest
import allure
import requests

class TestCourierCreation:
    @pytest.mark.usefixtures("register_new_courier", "delete_courier")
    @allure.title("Тест на создание курьера")
    def test_create_courier(self, register_new_courier, delete_courier):
        with allure.step("Генерируем нового курьера"):
            login, password, first_name = register_new_courier.values()

        # Проверяем, что данные курьера получены
        assert login and password and first_name, "Данные курьера не получены"

        with allure.step("Удаляем созданного курьера"):
            delete_courier(login)

    @pytest.mark.usefixtures("register_new_courier", "delete_courier")
    @allure.title("Тест на проверку, что нельзя создать двух одинаковых курьеров")
    def test_cannot_create_identical_couriers(self, register_new_courier, delete_courier):
        with allure.step("Генерируем нового курьера"):
            login, password, first_name = register_new_courier.values()

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        # Проверяем, что данные курьера получены и курьер успешно зарегистрирован фикстурой
        assert login and password and first_name, "Данные курьера не получены"

        with allure.step("Пытаемся создать второго курьера с теми же данными"):
            response_second = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', json=payload)

        with allure.step("Проверяем, что создание второго курьера завершилось ошибкой"):
            assert response_second.status_code == 409, \
                f"Ожидался код 409 для второго курьера, получен {response_second.status_code}"
            
            # Добавляем проверку тела ответа
            assert "message" in response_second.json(), "Ожидалось сообщение об ошибке в теле ответа"
            assert response_second.json()["message"] == "Этот логин уже используется", \
                "Ожидаемое сообщение об ошибке не совпадает с фактическим"

        # Удаление курьера после теста
        with allure.step("Удаляем созданного курьера"):
            delete_courier(login)

    @pytest.mark.usefixtures("delete_courier")
    @allure.title("Тест на проверку, что для создания курьера нужно передать все обязательные поля")
    def test_required_fields(self):
        with allure.step("Пытаемся создать курьера без указания некоторых полей"):
            payload_incomplete = {
                "login": "test_login",
                # password отсутствует
                "firstName": "test_name"
            }
            response_incomplete = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', json=payload_incomplete)

        with allure.step("Проверяем, что создание курьера завершилось ошибкой из-за отсутствия обязательных полей"):
            assert response_incomplete.status_code == 400, \
                f"Ожидался код 400 при отсутствии обязательных полей, получен {response_incomplete.status_code}"
            assert "message" in response_incomplete.json(), "Ожидалось сообщение об ошибке в теле ответа"

    @pytest.mark.usefixtures("register_new_courier", "delete_courier")
    @allure.title("Тест на проверку, что запрос возвращает правильный код ответа")
    def test_correct_response_code(self, register_new_courier, delete_courier):
        with allure.step("Генерируем нового курьера"):
            login, password, first_name = register_new_courier.values()

        # Проверяем, что данные курьера получены
        assert login and password and first_name, "Данные курьера не получены"

        # Удаление курьера после теста
        with allure.step("Удаляем созданного курьера"):
            delete_courier(login)

    @pytest.mark.usefixtures("register_new_courier", "delete_courier")
    @allure.title("Тест на проверку, что успешный запрос возвращает {'ok': True}")
    def test_ok_true(self, register_new_courier, delete_courier):
        with allure.step("Генерируем нового курьера"):
            login, password, first_name = register_new_courier.values()

        # Проверяем, что данные курьера получены
        assert login and password and first_name, "Данные курьера не получены"

        # Удаление курьера после теста
        with allure.step("Удаляем созданного курьера"):
            delete_courier(login)

    @pytest.mark.usefixtures("delete_courier")
    @allure.title("Тест на проверку, что если одного из полей нет, запрос возвращает ошибку")
    def test_missing_field(self, register_new_courier):
        with allure.step("Получаем данные курьера из фикстуры"):
            _, password, first_name = register_new_courier.values()

        with allure.step("Пытаемся создать курьера без одного из обязательных полей"):
            payload_missing_field = {
                # "login" отсутствует
                "password": password,
                "firstName": first_name
            }
            response_missing_field = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', json=payload_missing_field)

        with allure.step("Проверяем, что создание курьера завершилось ошибкой из-за отсутствия обязательных полей"):
            assert response_missing_field.status_code == 400, \
                f"Ожидался код 400 при отсутствии обязательных полей, получен {response_missing_field.status_code}"

            # Проверяем тело ответа
            assert "message" in response_missing_field.json(), "Ожидалось сообщение об ошибке в теле ответа"
            assert response_missing_field.json()["message"] == "Недостаточно данных для создания учетной записи", \
                "Ожидаемое сообщение об ошибке не совпадает с фактическим"

    @pytest.mark.usefixtures("register_new_courier", "delete_courier") 
    @allure.title("Тест на проверку, что если создать пользователя с логином, который уже есть, возвращается ошибка") 
    def test_existing_login(self, register_new_courier, delete_courier): 
        with allure.step("Генерируем нового курьера"):
            login, password, first_name = register_new_courier.values()

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        # Проверяем, что данные курьера получены и курьер успешно зарегистрирован фикстурой
        assert login and password and first_name, "Данные курьера не получены"

        with allure.step("Пытаемся создать второго курьера с теми же данными"):
            response_second = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', json=payload)

        with allure.step("Проверяем, что создание второго курьера завершилось ошибкой"):
            assert response_second.status_code == 409, \
                f"Ожидался код 409 для второго курьера, получен {response_second.status_code}"
            
            # Добавляем проверку тела ответа
            assert "message" in response_second.json(), "Ожидалось сообщение об ошибке в теле ответа"
            assert response_second.json()["message"] == "Этот логин уже используется", \
                "Ожидаемое сообщение об ошибке не совпадает с фактическим"

        # Удаление курьера после теста
        with allure.step("Удаляем созданного курьера"):
            delete_courier(login)