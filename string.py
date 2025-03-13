from userbot import API_ID, API_HASH
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

def main():
    print("Telefon nömrənizi yazın")

    client = TelegramClient(StringSession(), API_ID, API_HASH)
    client.start()
 
    string_session = client.session.save()
    print(f'\nAşağıdakı string sessionu kopyalayın:\n\n {string_session}\n')

if __name__ == "__main__":
    main()
