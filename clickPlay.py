import pyautogui
import keyboard
import time

# ultrawide settings
def click_at_position():
    pyautogui.click(950, 375)
    time.sleep(.3)

# rebinds up arrow to enter
def on_down_arrow():
    pyautogui.press('enter')
    time.sleep(.3)


# rebinds left to "hard"
def on_left_arrow():
    pyautogui.press('1')
    time.sleep(.3)

# rebinds right to "good"
def on_right_arrow():
    pyautogui.press('3')
    time.sleep(.3)


keyboard.add_hotkey('left', on_left_arrow)
keyboard.add_hotkey('right', on_right_arrow)
keyboard.add_hotkey('up', on_down_arrow)
keyboard.on_press_key('up', lambda _: click_at_position())

# waits til backtick is pressed (esc is used in the application)
keyboard.wait('`')
