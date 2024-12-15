import allure
import requests
import helper
import urls
from data import TestDataBody

class TestLoginCourier:

    @allure.title('Успешная авторизация')
    @allure.description('Проверяем успешную авторизацию с заполнением обязательных полей. С ответом 200 и возвратом id курьера, который не пустой')
    def test_success_login(self, default_courier):
        payload = default_courier
        requests.post(urls.URL_BASE + urls.URL_CREATE_COURIER, data=payload)
        response = requests.post(urls.URL_BASE + urls.URL_LOGIN, data=payload)
        assert response.status_code == 200 and response.json()["id"] is not None

    @allure.title('Авторизация курьером без одного обязательного к заполнению поля')
    @allure.description('Проверяем, что нельзя залогиниться без логина, приходит ожидаемый статус 400 и соответствующее письменное уведомление')
    def test_login_with_empty_data(self):
        response = requests.post(urls.URL_BASE + urls.URL_LOGIN, data=TestDataBody.BODY_WITHOUT_LOGIN)
        assert response.status_code == 400 and response.json()["message"] == TestDataBody.login_without_login_400_text

    @allure.title('Авторизация курьером с несуществующими данными')
    @allure.description('Проверяем, что нельзя авторизоваться под несуществующим пользователем, в логине. Приходит ответ 404 с соответствующим письменным уведомлением')
    def test_login_without_registration(self):
        payload = helper.TestMethodsHelper.create_random_login_password()
        response = requests.post(urls.URL_BASE + urls.URL_LOGIN, data=payload)
        assert response.status_code == 404 and response.json()["message"] == TestDataBody.login_without_reg_404_text
