from telethon.sync import TelegramClient
from telethon.sessions import StringSession

API_ID = 22590692
API_HASH = '471eb17c98d58856d25827c1af6584f6'

def main():
    print("Telefon nömrənizi yazın")

    client = TelegramClient(StringSession(), API_ID, API_HASH)
    client.start()
 
    string_session = client.session.save()
    print(f'\nAşağıdakı string sessionu kopyalayın:\n\n {string_session}\n')

if __name__ == "__main__":
    main()
