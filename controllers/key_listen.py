from pynput.keyboard import Key, Listener

import views.display
from controllers.input_mic import input_from_mic


def start_key_controller():
    # Collect events until released
    with Listener(
            on_release=on_release) as listener:
        listener.join()


def on_release(key):
    print('{0} release'.format(key))
    # TODO configファイルでキー設定をできるようにする->無理かも。初回時に設定するような仕組みのほうがいいかも
    if key == Key.ctrl_r:
        # 音声入力⇒クリップボード保存
        input_from_mic()

        # 画面表示
        views.display.init_display()

    if key == Key.esc:
        # Stop listener
        return False


if __name__ == '__main__':
    start_key_controller()
