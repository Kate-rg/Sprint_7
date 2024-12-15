import random
import string
import allure
import requests
import urls


class TestMethodsHelper:
    @staticmethod
    @allure.step('Создание рандомных регистрационных данных')
    def create_random_login_password():

        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        return {"login": login, "password": password, "firstName": first_name}

    @staticmethod
    @allure.step('Удаление курьера')
    def delete_courier(courier):
        response_id = requests.post(urls.URL_BASE + urls.URL_LOGIN, data=courier)
        id_number = response_id.json()["id"]
        requests.delete(f"{urls.URL_BASE}{urls.URL_DELETE_COURIER}{id_number}")