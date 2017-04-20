'''
	Author: Erik Zorn - Wallentin.
	Created: Mar. 25 / 2017.
	
	Sorry for the large file size! The submission did say to include example images.
	
	Report is in this directory called "A3ErikZornWallentin.doc or pdf version".
	
	Assignment 2 contains 6 testing images with the names:
	"1.png"
	"2.png"
	"3.png"
	"4.png"
	"5.png"
	"6.png"
	
	References: See the References.txt for more info, or see A3ErikZornWallentin.pdf for the reference list.
	
	Assignment 3 testing results after using all the algorithms in the folder named:
	"result" folder
	
	My code is all in the Python file called "a3.py" which contains more info below:
	*** IMPORTANT READ *** 
	The code will probably not compile on your computer because of the import settings, please change the import settings based on your computer!
	Which is probably not the same way yours is setup!
	
	Python libraries being used:
	Numpy, OpenCV, Imutils, PIL - Image
	
	*** IMPORTANT READ *** 
		
	This program was created for Assignment 3 in class CIS * 4720 (Image Processing & Vision).
		
	I used the OpenCV official documentation to complete this assignment, and some recommendations provided by the assignment and the professor.
		
	The program will attempt to use an RGB channel image from the Prokudin-Gorskii photo collection, and convert it to a coloured image.
	The image itself could have numerous problems, where there is a time gap of 1-3 minutes per image, could have small changes in the scene,
	and small nonlinear changes like clouds, water, changes etc.
	The goal of this assignment is to take into consideration of all these problems, fix them and give the output coloured photo.
	
	The program contains error checking in the menu, not on file provided.
	Use any image from 1-8.png.
	Example image to use: 1.png
		
	It starts off by waiting for user input with a menu displayed to the user.
	Menu:
		1) Images of the Russian Empire
		2) Quit the program (q)
	Choosing an option from the menu will allow you to do a specific task and ask for more input.
	Once it gives you the result from the task it will return you to the menu.
	
	Example Use:
		Choose menu option 1.
		Give the correct file on prompt with the file extension also (jpg) --> 1.png
		Wait a for the new filtered image to display, see the resulting files in the directory.
'''
