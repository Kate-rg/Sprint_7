import allure
import pytest
from helper import TestMethodsHelper


@allure.step('Создание нового курьера и удаление данных о курьере в конце теста')
@pytest.fixture(scope='function')
def default_courier():
    payload = TestMethodsHelper.create_random_login_password()
    yield payload

    TestMethodsHelper.delete_courier(payload)
