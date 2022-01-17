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


def hide_display_thread(window):
    # 何秒ディスプレイを表示
    time.sleep(5)
    window.write_event_value('-STOP-', '')


def hide_display():
    threading.Thread(target=hide_display_thread, args=(window,), daemon=True).start()


def show_display_voice_text():
    while True:
        event, values = window.read(timeout=500, timeout_key='-timeout-')
        # TODO 特定のキーが押されたらbreakするように設定
        if event == '-STOP-':
            break
        elif event in '-timeout-':
            window['-countdonw-'].update(show_count(count))
            window['-clipbord-'].update(pyperclip.paste())
            hide_display()
    window.close()


if __name__ == '__main__':
    init_display()
