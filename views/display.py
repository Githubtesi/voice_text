import threading
import time

import PySimpleGUI as sg
import pyperclip


def init_display():
    global window
    # テーマ設定
    sg.theme('Dark')
    layout = init_layout_voice_text()
    window = sg.Window('template', layout, keep_on_top=True)
    show_display_voice_text()


# レイアウト設定
def init_layout_voice_text():
    layout = [
        [sg.Text(size=(15, 1), font=('Helvetica', 15), justification='left', key='-countdonw-')],
        [sg.Text('', size=(20, 1), font=('Helvetica', 20), justification='center', key='-clipbord-')],
    ]
    return layout


# 音声認識の初期起動に1.5s必要
count = 2
display_time = 15


def countdown_thread():
    global count
    for _ in range(display_time):
        count -= 1
        time.sleep(1)


def show_count(count: int) -> str:
    if count >= 0:
        return str(count) + "秒待ってね"
    else:
        return "残り" + str(display_time + count - 2) + "秒"


def countdown():
    threading.Thread(target=countdown_thread, daemon=True).start()


def hide_display_thread(window):
    # 何秒ディスプレイを表示
    time.sleep(display_time)
    window.write_event_value('-STOP-', '')


def hide_display():
    threading.Thread(target=hide_display_thread, args=(window,), daemon=True).start()


def show_display_voice_text():
    global count
    countdown()
    hide_display()
    while True:
        event, values = window.read(timeout=500, timeout_key='-timeout-')
        if event == '-STOP-':
            count = 3
            break
        elif event in '-timeout-':
            window['-countdonw-'].update(show_count(count))
            window['-clipbord-'].update(pyperclip.paste())
    window.close()


if __name__ == '__main__':
    init_display()
