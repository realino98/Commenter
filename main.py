from datetime import date
import pyautogui

today = date.today()
print(today)

d1 = today.strftime("%d%m%y")
comment = "// BR_"+d1+"_"
print(comment)
pyautogui.write(comment)