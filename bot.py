from pydoc import cli
from telethon.sync import TelegramClient
from telethon import events, Button
import logging, json
import configparser
from owns import *

logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)




start = [
            [   
                Button.inline('شراء أرقام',"buy")
                ],

            [   
                Button.inline('طلباتي',"myorders"),  Button.inline('حسابي',"myaccount")
                ],
]

server_numbers = [
            [   
                Button.inline('السيرفر 2️⃣',"server|2"),  Button.inline('السيرفر 1️⃣',"server|1")
                ],
            [   
                Button.inline('السيرفر 3️⃣',"server|3")
                ],
]

config = configparser.ConfigParser() 
config.read("config.ini")

api_id = config['App']['id']
api_hash = config['App']['hash']
dev = json.loads(config['App']['dev'])
token = config['Token']['mybot']
client = TelegramClient('ses/bot', api_id, api_hash)
client.start(bot_token=token)
client.connect()

print('Running...')
client.send_message(879123322, 'Bot running..', buttons=Button.clear())


@client.on(events.NewMessage())
async def main(event):

    ms_id = event.message.id
    text = event.raw_text
    message = event.message
    fid = event.sender_id
    chat = event.chat_id
    ex = text.split(' ')
    #ban = read('data/ban.txt')
    #ban = ban.split("\n")
    

    if text == '/start':
        await event.reply('أهلا بك')
        return

@client.on(events.CallbackQuery)
async def callback(event):

    try:
        chat = event.original_update.peer.user_id
        dataa = event.data
        data = dataa.decode("utf-8")
        ex = data.split("-")
        ex_data = data.split("|")
    except Exception as er:
        print(er)
        data = False
    fid = event.sender_id
    #ban = read('data/ban.txt')
    #ban = ban.split("\n")
    print(data)
    if ex_data[0] == 'code':
        try:
            message = 'وصل الكود بنجاح إليك رسائل ال sms التي وصلت :'
            mes = ''
            code = api(1, 'code', id=ex_data[1])
            #print(code, 'ss')
            sms = code['sms']
            if len(sms) > 0:
                n = 1
                for i in sms:
                    ms = i['text']
                    c = i['code']
                    mes += "\n\n" + f"""
    الرسالة {n} : `{ms}`
    الكود {n} : `{c}`

                    """
                    
                    n += 1

                await event.reply(message + mes)
            else:
                await event.answer('لم يصل الكود بعد', alert=True)

        except Exception as rt:
            await event.answer('لم يصل الكود بعد', alert=True)
            print(rt)
            pass
        return


client.run_until_disconnected()