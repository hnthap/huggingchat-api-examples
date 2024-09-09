from contextlib import contextmanager
import os

from hugchat import hugchat
from hugchat.login import Login


def login(cookies_dir: str, email: str | None = None, password: str | None = None):
    if email is None:
        email = os.environ['HUGGING_FACE_EMAIL']
    if password is None:
        password = os.environ['HUGGING_FACE_PASSWORD']
    sign = Login(email, password)
    cookies = sign.login(cookie_dir_path=cookies_dir, save_cookies=True)
    return cookies


@contextmanager
def temporary_conversation(chatbot: hugchat.ChatBot, verbose = True):
    try:
        convo = chatbot.get_conversation_info()
        if verbose:
            print('Created a conversation with ID {} using {}'.format(convo.id, convo.model))
        yield convo
    except KeyboardInterrupt:
        pass
    finally:
        chatbot.delete_conversation(convo)