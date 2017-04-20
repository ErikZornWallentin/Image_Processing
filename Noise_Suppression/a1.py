'''
	Author: Erik Zorn - Wallentin.
	Created: Feb. 1 / 2017.
	
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

# The code will probably not compile on your computer because of the import settings, please change the import settings based on your computer!
# The only thing different from example code is "import Image" so look at mine and change depending on your system.
from PIL import Image
import numpy
import matplotlib.pyplot as plt
import scipy.ndimage.filters as nd
import pylab

# Added extra libraries to time functions.
import sys, timeit, datetime
import time

# Import the library provided from CIS*4720 class, the library file is in this directory.
# Please see imenh_lib.py file for the documentation and source code.
# Nothing was changed from imenh_library as I do not own this code.
import imenh_lib

'''
	Purpose: The main menu that is displayed to the user.
	Parameters: NONE.
	Return: NONE.
'''
def menu():
	print("\n\nPlease choose one of the following techniques for noise reduction using (1,2,3,4 or q):")
	print("1) Alpha-trimmed mean filtering")
	print("2) Truncated median 'mode' filtering")
	print("3) Hybrid median filtering")
	print("4) My First Algorithm: Gaussian filtering")
	print("5) My Second Algorithm: Rank filtering")
	print("6) Quit the program (q)")

'''
	Purpose: Gets the file given by the user using also the extension.
	Parameters: NONE.
	Return: file.
'''
def getFilename():
	filename = raw_input('Enter a file name with extension: ')
	return filename

'''
	Purpose: Reads in the file and returns the image.
	Parameters: file name given.
	Return: image.
'''
def imgRead(fname):
	imgIN = Image.open(fname) 
	if imgIN.mode == 'RGB': #colour
		img = numpy.asarray(imgIN)
	else: #grayscale
		img = numpy.asarray(imgIN)
	return (img)
	
# Function to read in a grayscale image and return as an 8-bit 2D array
def imread_colour(fname):
    img = PIL.Image.open(fname)
    imgRGB = np.asarray(img)
    imCr = imgRGB[:,:,0]
    imCg = imgRGB[:,:,1]
    imCb = imgRGB[:,:,2]
    return imCr, imCg, imCb

'''
	Purpose: Display grayscale (monochrome) of the image provided.
	Parameters: image.
	Return: NONE.
'''   
def imgGrayscaleDisplay(img):
	plt.imshow(img,cmap=plt.cm.gray)
	plt.show()

'''
	Purpose: Create a histogram and display it to the user.
	Parameters: image.
	Return: NONE.
'''   
def plotHistogram(img):
	plt.hist(img.ravel(), 256, range=(0,256)) #,histtype='step')
	plt.title("Grayscale Histogram")
	plt.xlabel("Bins")
	plt.ylabel("# of Pixels")
	plt.xlim([0, 256])
	plt.show()	
 
'''
	Purpose: The array hst contains the values in each of the 256 bins, the array bins contains the bing edges.
	Parameters: image.
	Return: histogram.
'''  
def imgHistogram(img):
	hst,bins = numpy.histogram(img.flatten(),256,(0,255),density=False)
	return hst
	
'''
	Purpose: My algorithm that performs gaussian filtering using scipy. Using standard deviation of 1.
	Parameters: image.
	Return: histogram.
'''  
def gaussianFiltering(img):
	#Ie = nd.gaussian_filter(input, sigma, order=0, output=None, mode='reflect', cval=0.0, truncate=4.0)
	Ie = nd.gaussian_filter(img, 1, order=0, output=None, mode='constant', cval=0.0, truncate=4.0)
	
	return Ie
	
'''
	Purpose: My algorithm that performs rank filtering using scipy. Using rank of 1.
	Parameters: image.
	Return: histogram.
'''  
def rankFiltering(img):
	kernel = numpy.array([[1, 1, 1, 1, 1],
						[1, 4, 4, 4, 1],
						[1, 4, 9, 4, 1],
						[1, 4, 4, 4, 1],
						[1, 1, 1, 1, 1]])

	#Ie = nd.rank_filter(input, rank, size=None, footprint=None, output=None, mode='reflect', cval=0.0, origin=0)
	Ie = nd.rank_filter(img, 1, size=None, footprint=kernel, output=None, mode='reflect', cval=0.0, origin=0)
	
	return Ie

def main():
	userInput = '0'
	checker = 1

	menu()

	while (checker == 1):
		userInput = raw_input("\nPlease enter a menu option: ")
		
		if (userInput == '1'):
			print ("\n\nUsing: Alpha-trimmed mean filtering")
		
			# Get file from user.
			filename = getFilename()
			# Get the image from the file.
			img = imgRead(filename)
			
			# Start Timing
			start_time = time.time()
			
			# Apply image processing filtering technique.
			filteredImg = imenh_lib.enh_alphaTMean(img, 0.5)
			
			# Display time taken to user.			
			print("\nAlpha-trimmed mean filtering took %s seconds to complete!" % (time.time() - start_time))
			
			# Display grayscale (monochrome) of the image result.
			imgGrayscaleDisplay(filteredImg)			
			
			# Display histogram of the image result.
			plotHistogram(filteredImg)
			
			# Display menu to user again.
			menu()
		elif (userInput == '2'):
			print ("\n\nUsing: Truncated median 'mode' filtering")
		
			# Get file from user.
			filename = getFilename()
			# Get the image from the file.
			img = imgRead(filename)
			
			# Start Timing
			start_time = time.time()
			
			# Apply image processing filtering technique.
			filteredImg = imenh_lib.enh_truncMedian(img)
			
			# Display time taken to user.			
			print("\nTruncated median 'mode' filtering took %s seconds to complete!" % (time.time() - start_time))
			
			# Display grayscale (monochrome) of the image result.
			imgGrayscaleDisplay(filteredImg)
			# Display histogram of the image result.
			plotHistogram(filteredImg)
			
			# Display menu to user again.
			menu()
		elif (userInput == '3'):
			print ("\n\nUsing: Hybrid median filtering")
		
			# Get file from user.
			filename = getFilename()
			# Get the image from the file.
			img = imgRead(filename)
			
			# Start Timing
			start_time = time.time()
			
			# Apply image processing filtering technique.
			filteredImg = imenh_lib.enh_hybridMedian(img)
			
			# Display time taken to user.			
			print("\nHybrid median filtering took %s seconds to complete!" % (time.time() - start_time))
			
			# Display grayscale (monochrome) of the image result.
			imgGrayscaleDisplay(filteredImg)
			# Display histogram of the image result.
			plotHistogram(filteredImg)
			
			# Display menu to user again.
			menu()
		elif (userInput == '4'):
			print ("\n\nUsing my first algorithm: Gaussian filtering")
		
			# Get file from user.
			filename = getFilename()
			# Get the image from the file.
			img = imgRead(filename)
			
			# Start Timing
			start_time = time.time()
			
			# Apply image processing filtering technique.
			filteredImg = gaussianFiltering(img)
			
			# Display time taken to user.			
			print("\nGaussian filtering took %s seconds to complete!" % (time.time() - start_time))
			
			# Display grayscale (monochrome) of the image result.
			imgGrayscaleDisplay(filteredImg)
			# Display histogram of the image result.
			plotHistogram(filteredImg)
			
			# Display menu to user again.
			menu()
		elif (userInput == '5'):
			print ("\n\nUsing my second algorithm: Rank filtering")
		
			# Get file from user.
			filename = getFilename()
			# Get the image from the file.
			img = imgRead(filename)
			
			# Start Timing
			start_time = time.time()
			
			# Apply image processing filtering technique.
			filteredImg = rankFiltering(img)
			
			# Display time taken to user.			
			print("\nRank filtering took %s seconds to complete!" % (time.time() - start_time))
			
			# Display grayscale (monochrome) of the image result.
			imgGrayscaleDisplay(filteredImg)
			# Display histogram of the image result.
			plotHistogram(filteredImg)
			
			# Display menu to user again.
			menu()
		elif (userInput == '6' or userInput == 'q'):
			print("\nNow quitting the program!\n")
			checker = 0
		else:
			print("Incorrect input, try again!\n")
			menu()

if __name__ == "__main__":
	main()