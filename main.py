import time
import vk_api

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


print("Рассылка началась!\n----------------\n")
for i in range(len(IDS)):
    time.sleep(1)
    try:
        send(i)
        print(f'сообщение {i} отправлено..')
    except vk_api.exceptions.Captcha as captcha:
        print('Ошибка вымени')
        captcha.sid # Получение sid
        captcha.get_url() # Получить ссылку на изображение капчи
        captcha.get_image() # Получить изображение капчи (jpg)
        send(i)