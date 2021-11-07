#Imports
import pyautogui
import keyboard
import winsound
import os
import time



#Var
pos = [["seek", 0, 0], ["pos1", 0, 0], ["pos2", 0, 0], ["pos3", 0, 0], ["pos4", 0, 0], ["pos5", 0, 0], ["pos6", 0, 0], ["pos7", 0, 0], ["pos8", 0, 0]]
inv = [[0, 0], [0, 0], [0,0],[0,0],[0,0],[0,0],[0,0]]
freq = 200
dur = 150

#Seek
#WIP: Loop loop
print("Open your and Navalis prophercies inventory(talk to her)!")
print("To be accurate, make sure that you have already filled all slots with prophercies")
print("Press Space to continue.")
keyboard.wait("space")
winsound.Beep(freq,dur)
os.system('cls')
#Pos1-9
print('Hover over the "Seek" button in Navalis inventory and press space')
keyboard.wait("space")
x, y = pyautogui.position()
pos[0][1]=x
pos[0][2]=y
winsound.Beep(freq, dur)
os.system('cls')

print("Hover over the 1st button in Navalis inventory and press space")
keyboard.wait("space")
x, y = pyautogui.position()
pos[1][1] = x
pos[1][2] = y
winsound.Beep(freq, dur)
os.system('cls')

print("Hover over the 2nd button in Navalis inventory and press space")
keyboard.wait("space")
x, y = pyautogui.position()
pos[2][1] = x
pos[2][2] = y
winsound.Beep(freq, dur)
os.system('cls')

print("Hover over the 3rd button in Navalis inventory and press space")
keyboard.wait("space")
x, y = pyautogui.position()
pos[3][1] = x
pos[3][2] = y
winsound.Beep(freq, dur)
os.system('cls')

print("Hover over the 4th button in Navalis inventory and press space")
keyboard.wait("space")
x, y = pyautogui.position()
pos[4][1] = x
pos[4][2] = y
winsound.Beep(freq, dur)
os.system('cls')

print("Hover over the 5th button in Navalis inventory and press space")
keyboard.wait("space")
x, y = pyautogui.position()
pos[5][1] = x
pos[5][2] = y
winsound.Beep(freq, dur)
os.system('cls')

print("Hover over the 6th button in Navalis inventory and press space")
keyboard.wait("space")
x, y = pyautogui.position()
pos[6][1] = x
pos[6][2] = y
winsound.Beep(freq, dur)
os.system('cls')

print("Hover over the 7th button in Navalis inventory and press space")
keyboard.wait("space")
x, y = pyautogui.position()
pos[7][1] = x
pos[7][2] = y
winsound.Beep(freq, dur)
os.system('cls')

print("Now we know all positions of her seek buttons.")
print('Seal one Prophercy and hover over the "Yes" button and press space')
keyboard.wait("space")
x, y = pyautogui.position()
pos[8][1] = x
pos[8][2] = y
winsound.Beep(freq, dur)
os.system('cls')


print("Now you need to select the Inventory Slots you want to use.")
print("Make sure you have them free our may ur items get destroyed!")
print("Hover your mouse over one slot and press space to select the next slot.")

try:
    row = 0
    col = 0
    while row != 7:
        print("Hover over the next slot!")
        keyboard.wait("space")
        x, y = pyautogui.position()
        inv[row][col] = x
        col+=1
        inv[row][col] = y
        col=0
        row+=1
        winsound.Beep(freq, dur)
except KeyboardInterrupt:
        print('\n')


try:
    while True:
        print("Now we have assigned all positions.")
        print("Press space to seek 8 Prophecies.")
        keyboard.wait("space")
        winsound.Beep(freq, dur)
        for i in range(1, 9):
            pyautogui.click(pos[0][1], pos[0][2])

        os.system("cls")

        print("Press Space to seal all prophecies.")
        keyboard.wait("space")

        row = 1
        col = 1
        for i in range(1, 8):
            pyautogui.moveTo(pos[row][col], pos[row][col+1])
            pyautogui.click()
            #time.sleep(1)
            pyautogui.moveTo(pos[8][1], pos[8][2])
            pyautogui.click()
            #time.sleep(1)
            pyautogui.moveTo(inv[row-1][col-1], inv[row-1][col])
            pyautogui.click()
            #time.sleep(1)
            row += 1
            col = 1
except KeyboardInterrupt:
        print('\n')
