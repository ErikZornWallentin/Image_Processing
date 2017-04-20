'''
	Author: Erik Zorn - Wallentin.
	Created: Feb. 1 / 2017.
	
	Sorry for the large file size! The submission did say to include example images.
	
	Part 1 and Part 2 of assignment are in Report.docx
	
	My code is for part 2 and the file is called a1.py
	
	a1.py details below?:
	
	*** IMPORTANT READ *** 
	The code will probably not compile on your computer because of the import settings, please change the import settings based on your computer!
	Which is probably not the same way yours is setup!
	*** IMPORTANT READ *** 
		
	This program was created for Assignment 1 in class CIS * 4720 (Image Processing & Vision).
		
	I used the class notes, and library provided by the professor which is located in this directory
	and it is called "imenh_lib.py" which holds some of the algorithms for noise suppression in image processing.
	I do not own the "imenh_lib.py" source code, and I did not modify the source code.
		
	The program will attempt to reduce noise in the images provided using specific noise suppression techniques.
	Noise suppression techniques used:
		From provided library
		- Alpha-trimmed mean filtering
		- Truncated median 'mode' filtering
		- Hybrid median filtering
		From my own implementation
		- Gaussian filtering
		- Rank filtering
	
	The program contains error checking in the menu, not on file provided.
		
	It starts off by waiting for user input with a menu displayed to the user.
	Menu:
		1) Alpha-trimmed mean filtering
		2) Truncated median 'mode' filtering
		3) Hybrid median filtering
		4) My First Algorithm: Gaussian filtering
		5) My Second Algorithm: Rank filtering
		6) Quit the program (q)
	Choosing an option from the menu will allow you to do a specific task and ask for more input.
	Once it gives you the result from the task it will return you to the menu.
	
	Example Use:
		Choose menu option 1.
		Give the correct file on prompt with the file extension also.
		Wait a few seconds for noise suppression technique to process.
		Look at your new image, compare it to given image.
		Exit out the given new image and a histogram will pop-up.
		Exit out of histogram and it will return you back to menu you try a different
		noise suppression technique.
		Can quit at any time by pressing q.
'''
'''