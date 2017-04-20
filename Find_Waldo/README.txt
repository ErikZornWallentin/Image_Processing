'''
	Author: Erik Zorn - Wallentin.
	Created: Feb. 28 / 2017.
	
	Sorry for the large file size! The submission did say to include example images.
	
	Report is in this directory called "A2ErikZornWallentin.doc or pdf version".
	
	Assignment 2 contains 8 testing images with the names:
	"1.jpg"
	"2.jpg"
	"3.jpg"
	"4.jpg"
	"5.jpg"
	"6.jpg"
	"7.jpg"
	"8.jpg"
	
	Assignment 2 template images for template matching (The template matching algorithm automatically uses them):
	"template1.jpg"
	"template2.jpg"
	"template3.jpg"
	"template4.jpg"
	"template5.jpg"
	"template6.jpg"
	"template7.jpg"
	"template8.jpg"
	
	References: See the References.txt for more info, or see A2ErikZornWallentin.pdf for the reference list.
	
	Assignment 2 testing results after using all the algorithms in the folder named:
	"Testing Results" folder
	
	My code is all in the Python file called "a2.py" which contains more info below:
	*** IMPORTANT READ *** 
	The code will probably not compile on your computer because of the import settings, please change the import settings based on your computer!
	Which is probably not the same way yours is setup!
	
	Python libraries being used:
	Numpy, OpenCV, Imutils
	
	*** IMPORTANT READ *** 
		
	This program was created for Assignment 2 in class CIS * 4720 (Image Processing & Vision).
		
	I used the class notes, and some algorithm code provided by the professor, and OpenCV official documentation to complete this assignment.
		
	The program will attempt to find Waldo based on 3 filters.
	1. Filter out everything that is not red and white and display new image.
	2. Filter out all colours that don't match the colour tone of Waldo and display new image.
	3. Display a blackbox around Waldo based on the template file provided.
	
	The program contains error checking in the menu, not on file provided.
		
	It starts off by waiting for user input with a menu displayed to the user.
	Menu:
		1) Red and white colour filtering
		2) Face tone filtering
		3) Template matching
		4) Quit the program (q)
	Choosing an option from the menu will allow you to do a specific task and ask for more input.
	Once it gives you the result from the task it will return you to the menu.
	
	Example Use:
		Choose menu option 1.
		Give the correct file on prompt with the file extension also (jpg).
		Wait a for the new filtered image to display.
		Choose a new menu option to filter the image.
'''
