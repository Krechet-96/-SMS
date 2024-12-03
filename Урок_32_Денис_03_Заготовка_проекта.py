import requests

user='user_name' # Своё имя будет
password='svoypassword'
sender='podpisotpravitelya'
receiver='79022604437'
text='Hello world!'

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
