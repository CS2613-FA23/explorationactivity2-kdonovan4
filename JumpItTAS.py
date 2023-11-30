import pyautogui
import time
from time import sleep

# Class to make and use a timer for timing the TAS
class Timer:
	def __init__(self):
		self.startTime = None

	def start(self):
		self.startTime = time.perf_counter()

	def stop(self):
		if self.startTime is None:
			return None
		elapsedTime = time.perf_counter() - self.startTime
		return elapsedTime

# Define the screen length and height
screenWidth, screenHeight = pyautogui.size()

# Display the first message box
option = pyautogui.confirm(text='This is a TAS (tool assistited speedrun) of my game from Exploration Activity 1\nDo you wish to proceed?', buttons=['Heck Ya', 'No Way'])

# Good ending
if option == "Heck Ya":
	pyautogui.alert(text='Make sure the game is in the middle of your main monitor and not covered by another window', button='Done')
	pyautogui.click(x= screenWidth/2, y= screenHeight/2)
	t = Timer()
	t.start()

	# First Jump
	pyautogui.keyDown('w')
	pyautogui.keyDown('d')
	sleep(0.17)
	pyautogui.keyUp('w')
	pyautogui.keyUp('d')


	# Second Jump
	with pyautogui.hold('d'):
			pyautogui.press(['w'])
	pyautogui.keyDown('d')
	sleep(0.45)
	pyautogui.keyUp('d')

	#Third Jump
	pyautogui.press('w')
	pyautogui.keyDown('d')
	sleep(0.22)
	pyautogui.keyUp('d')

	# Ending
	sleep(0.08)
	pyautogui.keyDown('d')
	sleep(0.25)
	pyautogui.keyUp('d')

	pyautogui.alert(text=f"Completed in: {t.stop():0.2f} seconds\nGame will now reset.", button='Cool')
	pyautogui.press('r')

# Bad Ending
else:
	pyautogui.alert(text='Wow, rude', button='I\'m sorry')