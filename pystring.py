 from telethon.sync import TelegramClient
 3 from telethon.sessions import StringSession
 4
 6 API_ID = 22590692
 7 API_HASH = '471eb17c98d58856d25827c1af6584f6'
 8
 9 def main():
10     print("Telefon nömrənizi yazın")
11
12     client = TelegramClient(StringSession(), API_ID, API_HASH)
13     client.start()
14
15     string_session = client.session.save()
16     print(f'\nString session: {string_session}\n')
17
18 if __name__ == "__main__":
19     main()
