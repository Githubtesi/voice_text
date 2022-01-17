import time

import PySimpleGUI as sg
import pyperclip

# 非同期チェック用として使用
def show_time():
    jikan = time.strftime('%p %I:%M:%S')
    return jikan


def init_display():
    global window
    # テーマ設定
    sg.theme('Dark')
    layout = init_layout_voice_text()
    window = sg.Window('template', layout)
    show_display_voice_text()


def init_layout_voice_text():
    # レイアウト設定
    layout = [
        [sg.Text(size=(15, 1), font=('Helvetica', 10), justification='center', key='-jikan-')],
        [sg.Text('Display', size=(20, 1), font=('Helvetica', 20), justification='center', key='-clipbord-')],
    ]
    return layout


def show_display_voice_text():
    while True:
        event, values = window.read(timeout=100, timeout_key='-timeout-')
        # TODO 特定のキーが押されたらbreakするように設定
        if event in (None, 'Cancel'):
            break
        elif event in '-timeout-':
            jikan = show_time()
            window['-jikan-'].update(jikan)
            window['-clipbord-'].update(pyperclip.paste())
    window.close()


if __name__ == '__main__':
    init_display()
