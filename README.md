## Which package/library does the sample program demonstrate?
The sample program, "JumpItTAS.py", demonstrates the PyAutoGUI library  

## How does someone run your program?
To run the program you first need to install both Arcade and PyAutoGUI with  
```pip install arcade``` and ```pip install pyautogui```  

For more information or OS specific installation instructions check these pages:  
[Python Arcade Installation Page](https://api.arcade.academy/en/latest/install/index.html)  
[PyAutoGUI Installation Page](https://pyautogui.readthedocs.io/en/latest/install.html)  

After both packages are installed make sure "JumpIt.py" and the assets folder are in the directory you wish to run the game from  
It can then be ran in the terminal using ```python JumpIt.py```  
In a separate terminal you can now run ```python JumpItTAS.py```  

## What purpose does your program serve?
My program is a tool-assisted speedrun (TAS) of the game I made for exploration activity 1. A TAS is basically a theoretically perfect speedrun, where the gameplay is not done by a human in real time, but rather by playing back a series of inputs. Typically these inputs are made by a person playing with tools such as slowing down the game or using savestates so the method I'm using is a very rudimentary and almost brute force way of passing in these inputs. Still, for a simple game like this, it serves its purpose. 
Additionally, it shows off much of what PyAutoGUI has to offer, including a mouse press, many keypresses, and a few message boxes.

## What would be some sample input/output?
The program will prompt you through a couple of message boxes to ensure that the game is set up properly, than if it is set up properly the game will run through on it's own. Make sure not to input any buttons on your own after pressing 'Done'. Because of processing times and how tight the jumps are, it may take a few run throughs to get a completion or it may not be possible on your pc.  

If you are unable to get a completion here is a recording of it being done on my pc, with the inputs shown in the top left corner:  
[Completion](https://imgur.com/pBaz4Wa)
