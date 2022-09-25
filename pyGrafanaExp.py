import secret
import setup
import os
import requests
from requests.structures import CaseInsensitiveDict
import telegram
import pdfkit
from html2image import Html2Image


def get_pic(url, token, filename):
    headers = CaseInsensitiveDict()
    headers["Authorization"] = "Bearer {}".format(token)
    resp = requests.get(url, headers=headers)

    print(resp.status_code)
    if not os.path.exists('./images'):
        os.makedirs('./images')
    with open('./images/{}'.format(filename), 'wb') as out_file:
        out_file.write(resp.content,)


def telegram_send_image(path):
    bot = telegram.Bot(secret.telegram_token)
    #path = './images/' + path
    try:
        print("Start send")
        bot.send_photo(secret.chat_id, photo=open(path, 'rb'))
        print("Send")
        return True
    except telegram.TelegramError as error_text:
        print(error_text)
        return False



def main():
    print("Hello")

    hti = Html2Image(custom_flags=['--virtual-time-budget=10000', '--hide-scrollbars'])

    #get_pic('http://10.150.2.3:3000/render/d-solo/t8s0rqzVk/databases?orgId=1&from=now-24d&to=now&panelId=2&width=1800&height=800&tz=Europe%2FMoscow', secret.grafana_token, 'dbcpu.png')
    #get_pic('http://10.150.2.3:3000/render/d-solo/t8s0rqzVk/databases?orgId=1&from=now-24h&to=now&panelId=4&width=1800&height=800&tz=Europe%2FMoscow', secret.grafana_token, 'dbloadavr.png')
    #get_pic('http://10.150.2.3:3000/render/d-solo/t8s0rqzVk/databases?orgId=1&from=now-24h&to=now&panelId=6&width=1800&height=800&tz=Europe%2FMoscow', secret.grafana_token, 'dbmemutil.png')
    #get_pic('http://10.150.2.3:3000/render/d-solo/t8s0rqzVk/databases?orgId=1&from=now-14d&to=now&panelId=8&width=1800&height=800&tz=Europe%2FMoscow', secret.grafana_token, 'dbfsutil.png')
    #get_pic('http://10.150.2.3:3000/render/d-solo/t8s0rqzVk/databases?orgId=1&from=now-24h&to=now&panelId=10&width=1800&height=800&tz=Europe%2FMoscow', secret.grafana_token, 'dbconn.png')
    #get_pic('http://10.150.2.3:3000/render/d-solo/t8s0rqzVk/databases?orgId=1&from=now-24h&to=now&panelId=12&width=1800&height=800&tz=Europe%2FMoscow', secret.grafana_token, 'dbcommroll.png')
    hti = Html2Image(custom_flags=['--virtual-time-budget=40000', '--hide-scrollbars'])
    hti.screenshot(url='http://10.150.2.3:3000/d/t8s0rqzVk/databases?orgId=1', save_as='db.png', size=(1920, 1400))
    hti1 = Html2Image(custom_flags=['--virtual-time-budget=40000', '--hide-scrollbars'])
    hti1.screenshot(url='http://10.150.2.3:3000/d/rBMOF6kVk/databases?orgId=1', save_as='app.png', size=(1920, 920))
    #pdfkit.from_url('http://10.150.2.3:3000/d/t8s0rqzVk/databases?orgId=1&from=1663590933941&to=1663612533941', 'out.pdf')
    telegram_send_image('db.png')
    telegram_send_image('app.png')
    #telegram_send_image('dbmemutil.png')
    #telegram_send_image('dbfsutil.png')
    #telegram_send_image('dbconn.png')
    #telegram_send_image('dbcommroll.png')

if __name__ == '__main__':
    main()


