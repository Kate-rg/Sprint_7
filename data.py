
class TestDataBody:

    BODY_WITHOUT_LOGIN = {"login": "",
                          "password": "1234567",
                          "firstName": "Катя"
                          }

    BODY_WITHOUT_FIRSTNAME = {"login": "gfjcbntr44",
                          "password": "1234567",
                          "firstName": ""
                          }

    courier_same_name_409_text = 'Этот логин уже используется. Попробуйте другой.'
    courier_without_login_400_text = 'Недостаточно данных для создания учетной записи'
    login_without_login_400_text = 'Недостаточно данных для входа'
    login_without_reg_404_text = 'Учетная запись не найдена'

    params_order_keys = 'firstName,lastName,address,metroStation,phone,rentTime,deliveryDate,comment,color'
    params_order_values = [
        ["Екатерина", "Бородина", "Кулакова 1,2", 3, "+7 123 456 78 90", 5, "2024-12-30", "звонить", ["BLACK"]],
        ["Екатерина", "Бородина", "Кулакова 1,2", 3, "+7 123 456 78 90", 5, "2024-12-30", "звонить", ["GREY"]],
        ["Екатерина", "Бородина", "Кулакова 1,2", 3, "+7 123 456 78 90", 5, "2024-12-30", "звонить", ["BLACK", "GREY"]],
        ["Екатерина", "Бородина", "Кулакова 1,2", 3, "+7 123 456 78 90", 5, "22024-12-30", "звонить", []]
    ]

