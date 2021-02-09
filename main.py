import os
from datetime import datetime as dt
import time
import vk_api

DELAY = 1
TOKEN = '<token>'
MESSAGE = 'Тестовое сообщение'
IDS = []

vk = vk_api.VkApi(token=TOKEN).get_api()


def send(id_):
    vk_id = IDS[id_]
    
    try:
        vk.messages.send(
            user_id=vk_id,
            message=MESSAGE + str(id_+1),
            random_id=0
        )
    except vk_api.exceptions.Captcha as captcha:
        print('Ошибка!\nВылезла капча..')
        
        captcha.sid
        with open('captcha.png', 'wb') as img:
            img.write(captcha.get_image())
        os.system('captcha.png')
        
        key = ''
        while key == '':
            key = input('Введите ответ: ')
        
        captcha.try_again(key)

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
    send(i)
    print(f'сообщение {i + 1} отправлено..')