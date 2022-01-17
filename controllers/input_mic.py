# -*- coding: utf-8 -*-
# Created by yoshiaki at 2022/01/18
import threading

import mojimoji
import pyperclip
import speech_recognition as sr


# need PyAudio-0.2.11-cp310-cp310-win_amd64
def input_from_mic_thread() -> str:
    pyperclip.copy('・・・音声認識中・・・')
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='ja-JP')
            query_str = "".join(query)
            query_str = mojimoji.zen_to_han(query_str)
            query_str = query_str.upper()
            query_str = query_str.replace(' ', '')
            pyperclip.copy(query_str)
        except Exception:
            return "Error"


def input_from_mic():
    threading.Thread(target=input_from_mic_thread, daemon=True).start()


if __name__ == "__main__":
    print(input_from_mic_thread())
