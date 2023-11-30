## Which package/library did you select?
I selected the package PyAutoGUI

## What is the package/library?
PyAutoGUI is a python package used to control the mouse and keyboard via a program. This means it can be used to automate tasks or in this case, speedrun a game. To use this package all you need to do is import it and implement the functions that will be covered in more detail in the next section. These functions mostly have to do with mouse movements/button presses and keyboard presses. On the mouse the left, middle, and right buttons can be pressed, but it is limited in that if you have a fancy mouse with other buttons it cannot control those. Same with the keyboard, pretty much any key can be used except for extra programmable buttons. Unlike the mouse, keyboards are much more varied in layout, meaning PyAutoGUI can allow you to press buttons you don't have on your current keyboard layout including all the way up to F24. Additionally PyAutoGUI integrates some other modules to allow extra functionality, such as PyScreeze for screenshots and locating on images or the screen, and PyMsgBox for the message box functions. To use the functions is pretty straightforward, as they don't require any classes and are executed proccedurally, meaning if you do something such as putting your cursor on a word document and execute the code  ```pyautogui.press('a')``` 
```pyautogui.press('b')```  
```pyautogui.press('c')```  
it will write "abc", just as one would expect.


## What are the functionalities of the package/library?
There are several functionalities provided by PyAutoGUI. The main ones are the ability to control the mouse and keyboard. 

To program mouse movements you have the option of moving it directly to a pixel on screen with ```pyautogui.moveTo(x, y)``` where x is the x-coordinate of where you wish to move to and y is the y-coordinate of where you wish to move to. You can also move the mouse in a direction relative to the current mouse position with ```pyautogui.move(x, y)``` where x and y are the distance in pixels that you wish to move in each respective direction (The current positon can be found using ```pyautogui.position()```). There are also functions to press the mouse buttons, the left one by default, and scroll. In my program I use a mouse click to click the center of the screen to make the game the active window using ```pyautogui.click(x= screenWidth/2, y= screenHeight/2)``` where ```screenWidth``` and ```screenHeight``` were previously stored using ```pyautogui.size()```.   

The bulk of my program is based on keyboard functions. Tt functions very similarly to the ```click()``` function for the mouse. You can use ```pyautogui.press(key)``` to press the majority of keys found on standard keyboards. The whole list of keys that can be press is the last section of [this](https://pyautogui.readthedocs.io/en/latest/keyboard.html) page. If you want to press more than one key at once, you can use ```with pyautogui.hold(key):``` to initiate the key you want pressed down with a series of other presses in the body. Alternatively you can use ```pyautogui.hotkey(keys)``` with a series of key strings as parameters which will push down in order and release in the opposite order. 

Additionally PyAutoGUI uses four message box functions from PyMsgBox; alert, confirm, prompt, and password.
For example, this code:    
```pyautogui.confirm(text='This is a TAS (tool assistited speedrun) of my game from Exploration Activity 1\nDo you wish to proceed?', buttons=['Heck Ya', 'No Way'])```  
Generates this message box:  
![TextBox](https://imgur.com/aWWpxOw.jpg)

The final functionality is the screenshot function. PyAutoGUI can take and parse images in order to locate objects on screen. This can be used in order to click on certain spots or perform inputs when something comes up on screen. I did not end up using this functionlity but it deserves to be mentioned regardless.

## When was it created?
The earliest version I'm able to find is Version 0.9.0, released on July 28th, 2014. The current version and the one that my sample program is built in is 0.9.54 released on May 24th, 2023 [[ref]](https://pypi.org/project/PyAutoGUI/#history).

## Why did you select this package/library?
I selected this package because I wanted to continue working on my program from Exploration Activity 1 but I couldn't find another library that provided a gamplay functionality that Arcade didn't already provide. Then I had the idea of creating a tool-assited speedrun of my game instead, so I found a library that would allow me to automate the inputs.

## How did learning the package/library influence your learning of the language?
In the end, I learned a lot more about problem solving than I did the language. I had to solve each jump individually than figure out how to link them together in what I hope is the most optimal way. Figuring out the sequence of inputs I thought of using a software to show keystrokes, meant for speedunners, and then record myself playing the game until I did it perfectly. Then I could pull up the recording and go frame by frame to see what I'd done and translate it as best I could into PyAutoGUI. It required lots of little tweaks but ended up being way simpler of a program than I had anticipated, so I used more of the functionalities to add the message boxes, and more of my general python knowledge that I've gained throughout the semester to add a timer at the end. It really ended up being an exercise of how far I could push a simple idea.

## How was your overall experience with the package/library?
I had a good experience with this package, it was fairly easy to use and understand. It was a little frustrating to used for something as precise as a TAS where frame-perfect timing is incredibly important, as processing time varied between runs so even though I found timings that work pretty consitantly, it will sometimes fail for no reason every few runs. This also means that the same timings may not work on another computer as well. Overall I would recommend this package to those looking to automate tasks that don't require a high level of precision involving timing (<0.1 of a second) as it otherwise provides great functionality with little confusion. Similarly, I would be willing use this package again, but not for a TAS as it was just a bit too inconsistant.
