import pyautogui
import keyboard

# ultrawide settings
def click_at_position():
    pyautogui.click(950, 375)


# rebinds up arrow to enter
def on_up_arrow():
    pyautogui.press('enter')


# rebinds left to "hard"
def on_left_arrow():
    pyautogui.press('1')


# rebinds right to "good"
def on_right_arrow():
    pyautogui.press('3')


keyboard.add_hotkey('left', on_left_arrow)
keyboard.add_hotkey('right', on_right_arrow)
keyboard.add_hotkey('up', on_up_arrow)
keyboard.on_press_key('down', lambda _: click_at_position())

# waits til backtick is pressed (esc is used in the application)
keyboard.wait('`')
