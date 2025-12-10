import pytest
import allure

class TestCourierAuthorization:
    @pytest.mark.usefixtures("register_new_courier", "delete_courier")
    @allure.title("Тест на проверку, что курьер может авторизоваться")
    def test_courier_can_authorize(self, register_new_courier, send_login_request, delete_courier):
        with allure.step("Получаем данные для авторизации курьера"):
            login, password = register_new_courier["login"], register_new_courier["password"]
        
        payload = {
            "login": login,
            "password": password
        }
        
        with allure.step("Отправляем запрос на авторизацию курьера"):
            response = send_login_request(payload)
        
        with allure.step("Проверяем, что ответ содержит ожидаемый код 200 и id курьера"):
            assert response.status_code == 200 and "id" in response.json(), \
                f"Ожидался код 200 и наличие id в ответе, получены {response.status_code} и {response.json()}"
        
        # Явный вызов delete_courier в конце теста
        with allure.step("Удаляем созданного курьера"):
            delete_courier(login)

    @pytest.mark.usefixtures("delete_courier")
    @allure.title("Тест на проверку, что для авторизации нужно передать все обязательные поля, а также если какого-то поля нет, запрос возвращает ошибку")
    def test_missing_login(self, send_login_request):
        with allure.step("Формируем payload без логина"):
            payload = {
                "password": "examplepassword"
            }
    
        with allure.step("Отправляем запрос на авторизацию"):
            response = send_login_request(payload)
    
        with allure.step("Проверяем, что ответ содержит ожидаемый код 400 и сообщение об ошибке"):
            assert response.status_code == 400, \
                f"Ожидался код 400 при отсутствии логина, получен {response.status_code}"
            assert "message" in response.json(), \
                "Ожидалось наличие сообщения 'message' в теле ответа"
            assert response.json()["message"] == "Недостаточно данных для входа", \
                f"Ожидается сообщение 'Недостаточно данных для входа', получено '{response.json()['message']}'"
            
    @pytest.mark.usefixtures("register_new_courier", "delete_courier")
    @allure.title("Тест на проверку, что система вернёт ошибку, если неправильно указать логин")
    def test_wrong_login(self, register_new_courier, send_login_request):
        with allure.step("Получаем данные для авторизации курьера"):
            correct_password = register_new_courier["password"]
    
        with allure.step("Формируем payload с неправильным логином"):
            payload = {
                "login": "terstkjrsgfghjs",
                "password": correct_password
            }
    
        with allure.step("Отправляем запрос на авторизацию"):
            response = send_login_request(payload)
    
        with allure.step("Проверяем, что ответ содержит ожидаемый код 404 и сообщение об ошибке"):
            assert response.status_code == 404, \
                f"Ожидался код 404 при неправильном логине, получен {response.status_code}"
            assert "message" in response.json(), \
                "Ожидалось наличие сообщения 'message' в теле ответа"
            assert response.json()["message"] == "Учетная запись не найдена", \
                f"Ожидается сообщение 'Учетная запись не найдена', получено '{response.json()['message']}'"
            
    @pytest.mark.usefixtures("register_new_courier", "delete_courier")
    @allure.title("Тест на проверку, что система вернёт ошибку, если неправильно указать пароль")
    def test_wrong_password(self, register_new_courier, send_login_request):
        with allure.step("Получаем данные для авторизации курьера"):
            login = register_new_courier["login"]
    
        with allure.step("Формируем payload с неправильным паролем"):
            payload = {
                "login": login,
                "password": "wrongpassword"
            }
    
        with allure.step("Отправляем запрос на авторизацию"):
            response = send_login_request(payload)
    
        with allure.step("Проверяем, что ответ содержит ожидаемый код 404 и сообщение об ошибке"):
            assert response.status_code == 404, \
                f"Ожидался код 404 при неправильном пароле, получен {response.status_code}"
            assert "message" in response.json(), \
                "Ожидалось наличие сообщения 'message' в теле ответа"
            assert response.json()["message"] == "Учетная запись не найдена", \
                f"Ожидается сообщение 'Учетная запись не найдена', получено '{response.json()['message']}'"
            
    @pytest.mark.usefixtures("delete_courier")
    @allure.title("Тест на проверку, что при авторизации под несуществующим пользователем возвращается ошибка")
    def test_non_existent_user(self, send_login_request):
        with allure.step("Формируем payload с несуществующим логином и паролем"):
            payload = {
                "login": "nonexisttttent",
                "password": "nonexistentpassword"
            }
        
        with allure.step("Отправляем запрос на авторизацию"):
            response = send_login_request(payload)
        
        with allure.step("Проверяем, что ответ содержит ожидаемый код 404 и сообщение об ошибке"):
            assert response.status_code == 404, \
                f"Ожидался код 404 при попытке авторизации несуществующим пользователем, получен {response.status_code}"
            assert "message" in response.json(), \
                "Ожидалось наличие сообщения 'message' в теле ответа"
            assert response.json()["message"] == "Учетная запись не найдена", \
                f"Ожидается сообщение 'Учетная запись не найдена', получено '{response.json()['message']}'"
            
    @pytest.mark.usefixtures("register_new_courier", "delete_courier")
    @allure.title("Тест на проверку, что успешный запрос на авторизацию возвращает id курьера")
    def test_successful_authorization_returns_id(self, register_new_courier, send_login_request):
        with allure.step("Получаем данные для успешной авторизации курьера"):
            login = register_new_courier["login"]
            password = register_new_courier["password"]
        
        with allure.step("Формируем payload с корректными данными для авторизации"):
            payload = {
                "login": login,
                "password": password
            }
        
        with allure.step("Отправляем запрос на авторизацию"):
            response = send_login_request(payload)
        
        with allure.step("Проверяем, что ответ содержит ожидаемый код 200 и 'id' в теле ответа"):
            error_message = (
                f"Ожидался код 200 и наличие 'id' в ответе, получены: "
                f"status code - {response.status_code}, "
                f"response json - {response.json()}"
            )
            assert response.status_code == 200 and "id" in response.json(), error_message