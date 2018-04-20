import requests
import time
#from telegram import ReplyKeyboardMarkup
url = "https://api.telegram.org/bot<>/"
reply_keyboard = [['AC', 'NonAC']]
#markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

def get_updates_json(request):  
    response = requests.get(request + 'getUpdates')
    return response.json()


def last_update(data):  
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]
def get_chat_id(update):  
    chat_id = update['message']['chat']['id']
    return chat_id

def send_mess(chat, text):  
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response


def main():  
    update_id = last_update(get_updates_json(url))['update_id']
    while True:
        if update_id == last_update(get_updates_json(url))['update_id']:
           send_mess(get_chat_id(last_update(get_updates_json(url))), 'Welcome to Hotel mYVeg, would you like book for dinner or lunch')
           update_id += 1
    sleep(1)       

if __name__ == '__main__':  
    main()
