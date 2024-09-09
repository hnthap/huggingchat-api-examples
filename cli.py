import os

from dotenv import load_dotenv
from hugchat import hugchat
from hugchat.exceptions import ChatError

from chatter import login, temporary_conversation


CURRENT_DIR = os.path.abspath(os.path.join(__file__, '..'))
COOKIES_DIR = os.path.join(CURRENT_DIR, 'cookies')


def main():
    load_dotenv(os.path.join(CURRENT_DIR, '.env'))
    cookies = login(COOKIES_DIR)
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    with temporary_conversation(chatbot):
        print('To exit, type "\\" and enter.')
        while True:
            message = input('> ')
            if message.strip() == '\\':
                break
            while True:
                try:
                    response_message = chatbot.chat(message)
                except ChatError as e:
                    if '"Model is overloaded"' in str(e):
                        print('Model is overloaded. Trying again...')
                        continue
                    else:
                        raise e
                break
            print()
            print(response_message)


if __name__ == '__main__':
    main()
