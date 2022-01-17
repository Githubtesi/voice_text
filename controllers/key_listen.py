from pynput.keyboard import Key, Listener

import views.display

is_show = True
is_not_show = not is_show


def on_press(key):
    print('{0} pressed'.format(key))
    if key == Key.ctrl_r:
        views.display.init_display()


def on_release(key):
    print('{0} release'.format(key))
    if key == Key.ctrl_r:
        views.display.close_window()

    if key == Key.esc:
        # Stop listener
        return False


# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
