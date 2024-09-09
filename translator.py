import os
import time

from dotenv import load_dotenv
from hugchat import hugchat
from hugchat.login import Login
from hugchat.exceptions import ChatError


CURRENT_DIR = os.path.abspath(os.path.join(__file__, '..'))
COOKIES_DIR = os.path.join(CURRENT_DIR, 'cookies')


if __name__ == '__main__':

    original_language = 'Vietnamese'
    target_language = 'English'

    # List of sentences that need to be translated
    sentences = [
        'Trăm năm trong cõi người ta, chữ tài chữ mệnh khéo là ghét nhau.',
        'Cảo thơm lần giở trước đèn, phong tình cổ lục còn truyền sử xanh.',
        'Rô-ma là một thành phố của nước Ý.',
    ]

    load_dotenv(os.path.join(CURRENT_DIR, '.env'))
    email = os.environ['HUGGING_FACE_EMAIL']
    password = os.environ['HUGGING_FACE_PASSWORD']
    sign = Login(email, password)
    cookies = sign.login(cookie_dir_path=COOKIES_DIR, save_cookies=True)
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    translated_sentences: list[str] = []
    for sentence in sentences:
        message = 'Translate this sentence from {0} into {1}: "{2}". Response the translation without any further explanations.'.format(original_language, target_language, sentence)
        while True:
            try:
                response = chatbot.chat(message)
            except ChatError as e:
                if '"Model is overloaded"' in str(e):
                    print('Model is overloaded. Trying again...')
                    time.sleep(1)
                    continue
                else:
                    raise e
            break
        translated_sentences.append(response.text)
    convo = chatbot.get_conversation_info()
    chatbot.delete_conversation(convo)
    for sentence in translated_sentences:
        print(sentence)


