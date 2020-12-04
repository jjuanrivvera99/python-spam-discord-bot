import pyautogui, time, random, string

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

time.sleep(5)

while True:
    pyautogui.typewrite(get_random_string(8))
    pyautogui.press("enter")
    time.sleep(60)