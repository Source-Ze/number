from pydoc import cli
from owns import *
import configparser
from telethon.sync import TelegramClient
from telethon import Button

config = configparser.ConfigParser() 
config.read("config.ini")

api_id = config['App']['id']
api_hash = config['App']['hash']
dev = json.loads(config['App']['dev'])
token = config['Token']['mybot']
#while True:


try:
    buy =  api(1, 'buy', 'kuwait', 'any', 'whatsapp')
    #buy =  api(1, 'buy', 'mongolia', 'any', 'telegram')
    print(buy)
    id = buy['id']
    price = buy['price']
    phone = buy['phone']
    country = buy['country']


    client = TelegramClient('ses/ir', api_id, api_hash)
    client.start(bot_token=token)
    client.connect()
    num = [
        [   
                Button.inline('الحصول على الكود',"code|"+str(id))
                ],
    ]
    for i in dev:
        client.send_message(i, f"""
تم شراء رقم بنجاح..

الدولة : الكويت
الرقم : `{phone}`
السعر : `{price}`
معرف العملية: `{id}`
whatsapp
    
..
        """, buttons=num)

    client.disconnect()

except Exception as er:
    print(er)
    pass