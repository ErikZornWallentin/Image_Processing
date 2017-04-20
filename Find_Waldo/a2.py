'''
	Author: Erik Zorn - Wallentin.
	Created: Feb. 28 / 2017.
	
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

# The code will probably not compile on your computer because of the import settings, please change the import settings based on your computer!
# Also download the proper python libraries: Numpy, OpenCV, Imutils.

#import pylab
import numpy as np
#import matplotlib.pyplot as plt
#import colorsys
#from PIL import Image

#import argparse
import imutils
import cv2


# Added extra libraries to time functions.
import sys, timeit, datetime
import time

'''
	Purpose: The main menu that is displayed to the user.
	Parameters: NONE.
	Return: NONE.
'''
def menu():
	print("\n\nPlease choose one of the following techniques for noise reduction using (1,2,3,4 or q):")
	print("1) Red and white colour filtering")
	print("2) Face tone filtering")
	print("3) Template matching")
	print("4) Quit the program (q)")

'''
	Purpose: Gets the file given by the user using also the extension.
	Parameters: NONE.
	Return: file.
'''
def getFilename():
	filename = raw_input('Enter a file name with extension: ')
	return filename

def main():
	userInput = '0'
	checker = 1

	menu()

	while (checker == 1):
		userInput = raw_input("\nPlease enter a menu option: ")
		
		if (userInput == '1'):
			print ("\n\nUsing: Red and white colour filtering")
			print ("Choose image between 1-8 Ex: 1.jpg")
			
			# Start Timing
			start_time = time.time()
			
			fileName = getFilename()
			image = cv2.imread(fileName)			
			
			lowerR = 50
			lowerG = 0
			lowerB = 0
			
			upperR = 255
			upperG = 100
			upperB = 100

			redBoundary = [
				#G,B,R
				([lowerG, lowerB, lowerR], [upperG, upperB, upperR]),
			]
			
			lowerR = 170
			lowerG = 180
			lowerB = 160
			
			upperR = 255
			upperG = 255
			upperB = 255
			
			whiteBoundary = [
				#G,B,R
				([lowerG, lowerB, lowerR], [upperG, upperB, upperR]),
			]
			
			redMask = "";
			whiteMask = "";
			redOutput = "";
			whiteOutput = "";
			redAndWhiteOutput = "";
			
			# Test the image for Red Colours
			for (lower, upper) in redBoundary:
				# create NumPy arrays from the boundaries
				lower = np.array(lower, dtype = "uint8")
				upper = np.array(upper, dtype = "uint8")
			 
				redMask = cv2.inRange(image, lower, upper)
				redOutput = cv2.bitwise_and(image, image, mask = redMask)
				
			# Test the image for White Colours
			for (lower, upper) in whiteBoundary:
				# create NumPy arrays from the boundaries
				lower = np.array(lower, dtype = "uint8")
				upper = np.array(upper, dtype = "uint8")
			 
				whiteMask = cv2.inRange(image, lower, upper)
				whiteOutput = cv2.bitwise_and(image, image, mask = whiteMask)
			 
			redAndWhiteOutput =  cv2.addWeighted(redOutput, 1, whiteOutput, 1, 0)
			
			# Display time taken to user.			
			print("\nRed and white colour filtering took %s seconds to complete!" % (time.time() - start_time))	
			 
			#cv2.imshow("RedFilter", imutils.resize(np.hstack([image, redOutput]), height = 900))
			#cv2.imshow("WhiteFilter", imutils.resize(np.hstack([image, whiteOutput]), height = 900))
			cv2.imshow("Red and White Filter", imutils.resize(np.hstack([redAndWhiteOutput]), height = 900))
			cv2.waitKey(0)
			
			# Display menu to user again.
			menu()
		if (userInput == '2'):
			print ("\n\nUsing: Face tone filtering")
			print ("Choose image between 1-8 Ex: 1.jpg")
			
			# Start Timing
			start_time = time.time()
			
			fileName = getFilename()
			image = cv2.imread(fileName)
			
			
			lowerR = 160
			lowerG = 125
			lowerB = 60
			
			upperR = 255
			upperG = 240
			upperB = 240

			faceToneBoundary = [
				#G,B,R
				([lowerG, lowerB, lowerR], [upperG, upperB, upperR]),
			]
			
			faceToneMask = "";
			faceToneOutput = "";
			
			# Test the image for Red Colours
			for (lower, upper) in faceToneBoundary:
				# create NumPy arrays from the boundaries
				lower = np.array(lower, dtype = "uint8")
				upper = np.array(upper, dtype = "uint8")
			 
				faceToneMask = cv2.inRange(image, lower, upper)
				faceToneOutput = cv2.bitwise_and(image, image, mask = faceToneMask)
			
			# Display time taken to user.			
			print("\nFace tone filtering took %s seconds to complete!" % (time.time() - start_time))	

			cv2.imshow("Face Tone Filter", imutils.resize(np.hstack([faceToneOutput]), height = 900))
			cv2.waitKey(0)
			
			# Display menu to user again.
			menu()
		elif (userInput == '3'):
			print ("\n\nUsing: Template matching")
			print ("Choose image between 1-8 Ex: 1.jpg")
			
			# Start Timing
			start_time = time.time()
			
			fileName = getFilename()
			image = cv2.imread(fileName)
			template = cv2.imread("template1.jpg")
			if (fileName == "1.jpg"):
				template = cv2.imread("template1.jpg")
			elif (fileName == "2.jpg"):
				template = cv2.imread("template2.jpg")
			elif (fileName == "3.jpg"):
				template = cv2.imread("template3.jpg")
			elif (fileName == "4.jpg"):
				template = cv2.imread("template4.jpg")
			elif (fileName == "5.jpg"):
				template = cv2.imread("template5.jpg")
			elif (fileName == "6.jpg"):
				template = cv2.imread("template6.jpg")
			elif (fileName == "7.jpg"):
				template = cv2.imread("template7.jpg")
			elif (fileName == "8.jpg"):
				template = cv2.imread("template8.jpg")
					
			(height, width) = template.shape[0:2]
			
			# Find waldo using the template
			templateResult = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
			threshold = 0.8
			loc = np.where( templateResult >= threshold)
			for pt in zip(*loc[::-1]):
				cv2.rectangle(image, pt, (pt[0] + width, pt[1] + height), (0,0,0), 5)
			
			# Display time taken to user.			
			print("\nTemplate matching took %s seconds to complete!" % (time.time() - start_time))	
			 
			cv2.imshow("Template Matching", imutils.resize(image, height = 900))
			cv2.waitKey(0)	
			
			# Display menu to user again.
			menu()
		elif (userInput == '4' or userInput == 'q'):
			print("\nNow quitting the program!\n")
			checker = 0
		else:
			print("Incorrect input, try again!\n")
			menu()

if __name__ == "__main__":
	main()