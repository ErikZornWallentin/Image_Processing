'''
	Author: Erik Zorn - Wallentin.
	Created: Mar. 25 / 2017.
	
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

# The code will probably not compile on your computer because of the import settings, please change the import settings based on your computer!
# Also download the proper python libraries: Numpy, OpenCV, Imutils.

from PIL import Image
from PIL import ImageChops
import numpy as np
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
	print("\n\nPlease choose one of the following techniques for noise reduction using (1,2 or q):")
	print("1) Images of the Russian Empire")
	print("4) Quit the program (q)")

'''
	Purpose: Gets the file given by the user using also the extension.
	Parameters: NONE.
	Return: file.
'''
def getFilename():
	filename = raw_input('Enter a file name with extension: ')
	return filename
	
'''
	Purpose: Split the base image into the 3 images which also happen to be RGB Channels.
	Parameters: img (source image to split).
	Return: Split image in the RGB channels.
'''
def split(img):	
	width, height = img.size
	totalHeight = height / 3
	halfHeight = totalHeight * 2
	
	rImg = img.crop((0, halfHeight, width, totalHeight * 3))
	gImg = img.crop((0, totalHeight, width, halfHeight))
	bImg = img.crop((0, 0, width, totalHeight))
	
	return rImg, gImg, bImg
    
'''
	Purpose: Aligns the given images, based on the normalized cross-correlation of the two images.
	         Recommended by L14 from CourseLink in CIS*4720 class.
	Parameters: firstImg (source image), secondImg (image to align to source).
	Return: Aligned image.
'''
def alignment(firstImg, secondImg):
	pixelAmount = 40
	minAmount = 0
	alignedX = 0
	alignedY = 0
	
	print "Please wait for alignment..."
	
	for x in range(-pixelAmount, pixelAmount + 1):
		for y in range(-pixelAmount, pixelAmount + 1):
			# Image is displaced by x / y pixel amounts in horizontal / vertical directions.
			offset = ImageChops.offset(secondImg, x, y)
			amount = np.sum(firstImg / np.linalg.norm(firstImg) * offset / np.linalg.norm(offset))
			#print amount
			
			# Check if the max alignment amount is greater than the minimum amount.
			if amount > minAmount:
				minAmount = amount
				alignedX = x
				alignedY = y

	return alignedX, alignedY

def main():
	userInput = '0'
	checker = 1
	
	menu()
	
	while (checker == 1):
		userInput = raw_input("\nPlease enter a menu option: ")
		
		if (userInput == '1'):
			print ("\n\nUsing: Images of the Russian Empire")
			print ("Choose image between 1-8.png Ex: 1.png")
	
			# Start Timing
			start_time = time.time()
			
			filename = getFilename()
			# Can hardcode the filename instead, just switch comment below.
			img = Image.open(filename)
			#img = Image.open("1.png")
			width, height = img.size
			img = img.point(lambda n:n * (1. / 255)).convert('L')
			img.mode = 'I'
			
			# Crop the image based on the given dimensions.
			croppedTop = int(height * 0.04)
			croppedBottom = int(height * 0.02)
			croppedLeft = int(width * 0.02)
			croppedRight = int(width * 0.05)		
			img = img.crop((croppedLeft, croppedTop, width - croppedRight, height - croppedBottom))
	
			# Resizing the image, as it would take forever to process in the current dimensions.
			# Don't have time to wait for long processing.
			array = np.asarray(img)
			resizedImg = cv2.resize(array, (0,0), fx = 0.1, fy = 0.1)
			resizedImg = Image.fromarray(resizedImg)
	
			# Split the image into 3 sections channels.
			rImg, gImg, bImg = split(resizedImg)
	
			tupleGB = alignment(bImg, gImg)
			tupleRB = alignment(bImg, rImg)
			scalarGB = tuple(i * 10 for i in tupleGB)
			scalarRB = tuple(i * 10 for i in tupleRB)
	
			# Align the G / R inverted negative to the B inverted negative,
			# and apply the shifted factor, based on the rescale value.
			rImg, gImg, bImg = split(img)
			#rImg = ImageChops.offset(rImg, scalarRB[0], scalarRB[1])
			#gImg = ImageChops.offset(gImg, scalarGB[0], scalarGB[1])
	
			rImg = np.asarray(rImg)
			gImg = np.asarray(gImg)
			bImg = np.asarray(bImg)
			img = cv2.merge((bImg, gImg, rImg))
			
			cv2.imwrite('red.jpg', rImg)
			cv2.imwrite('blue.jpg', bImg)
			cv2.imwrite('green.jpg', gImg)
			cv2.imwrite('result.jpg', img)
	
			# Show final output.
			result = cv2.imread('result.jpg', cv2.IMREAD_COLOR)
			cv2.imshow("Merged Color Image", imutils.resize(np.hstack([result]), height = 800))
			cv2.waitKey(0)
			cv2.destroyAllWindows()
	
			# Display time taken to user.			
			print("\nImages of the Russian Empire took %s seconds to complete!" % (time.time() - start_time))	
	
			# Display menu to user again.
			menu()
		elif (userInput == '2' or userInput == 'q'):
			print("\nNow quitting the program!\n")
			checker = 0
		else:
			print("Incorrect input, try again!\n")
			menu()
	
if __name__ == "__main__":
	main()