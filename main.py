from datetime import datetime as dt
import time
import vk_api

DELAY = 1
TOKEN = '<token>'
MESSAGE = 'Тестовое сообщение'
IDS = []

def send(id_):
    vk_id = IDS[id_]
    msg = MESSAGE
    
    vk.messages.send(
        user_id=vk_id,
        message=msg,
        random_id=0
    )

vk = vk_api.VkApi(token=TOKEN).get_api()

while True:
    start_time = input('Введите время начала рассылки в формате "ЧЧ:ММ": ')
    try:
        start_time = dt.timestamp(
            dt.combine(dt.date(dt.now()), 
                        dt.time(dt.strptime(start_time, '%H:%M'))
                        )
            )
        break
    except ValueError:
        print('Неверный формат!')

print('Ожидаем начала рассылки..', end='\r')
while dt.timestamp(dt.now()) < start_time:
    time.sleep(1)

print("Рассылка началась!       \n----------------\n")
for i in range(len(IDS)):
    time.sleep(DELAY)
    try:
        send(i)
        print(f'сообщение {i} отправлено..')
    except vk_api.exceptions.Captcha as captcha:
        print('Ошибка вымени')
        captcha.sid # Получение sid
        captcha.get_url() # Получить ссылку на изображение капчи
        captcha.get_image() # Получить изображение капчи (jpg)
        send(i)
