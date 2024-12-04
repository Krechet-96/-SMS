import requests
import re
import json


def check_balance(login, password):
    url = "https://my3.webcom.mobi/xml/balance.php"
    headers = {"Content-type": "text/xml; charset=utf-8"}

    data = {"login": login,
            "password": password}
    try:
        response = requests.post(url, data=json.dumps(data), headers=headers)

        if response.status_code == 200:
            response_data = response.json()
            print(response_data)
            print(f"Баланс: {response_data["money"]}")
        else:
            print(f"Произошла ошибка {response.status_code}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка {e}")


def validate_phone_number(phone_number):
    pattern = r'^79\d{9}$'
    return bool(re.match(pattern, phone_number))


user='user_name' # Своё имя будет
password='svoypassword'
sender='podpisotpravitelya'
receiver='790226044371'
text='Hello world!'

balance = check_balance(user, password)
if balance:
    if balance > 10:
        if not validate_phone_number(receiver):
            print("Ошибка! Некорректный номер ")
        else:
            url=f"https://my3.webcom.mobi/sendsms.php?user={user}&pwd={password}&sadr={sender}&dadr={receiver}&text={text}"
            print(url)
            try:
                response = requests.get(url)
                print(response)

                if response.status_code == 200:
                    print("Сообщение успешно отправлено!")
                else:
                    print(f"Ошибка при отправке сообщения {response.status_code}")
            except Exception as e:
                print(f"Непредвиденная ошибка с кодом {e}")
    else:
        print("Недостаточно средств")
else:
    print("Не удалось получить информацию о балансе")
