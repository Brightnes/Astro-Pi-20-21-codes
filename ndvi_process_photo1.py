"""
Slightly modified.
The line reporting
 bluSat[ndvi>128] = 0;
was, originally:
 bluSat[ndvi>=128] = 0;
but I deleted the '=' to avoid oddity at pure green color
"""
import numpy as np #arrays and math
import cv2 #opencv library
import matplotlib.pyplot as plt
from PIL import Image

#-------------------------------------------
#----------------NDVI Function--------------
#-------------------------------------------

#NDVI Calculation
#Input: an RGB image frame from infrablue source (blue is blue, red is pretty much infrared)
#Output: an RGB frame with equivalent NDVI of the input frame

def NDVICalc(original):
    "This function performs the NDVI calculation and returns an RGB frame)"
    lowerLimit = 5 #this is to avoid divide by zero and other weird stuff when color is near black

    #First, make containers
    oldHeight,oldWidth = original[:,:,0].shape; 
    ndviImage = np.zeros((oldHeight,oldWidth,3),np.uint8) #make a blank RGB image
    ndvi = np.zeros((oldHeight,oldWidth),np.int) #make a blank b/w image for storing NDVI value
    red = np.zeros((oldHeight,oldWidth),np.int) #make a blank array for red
    blue = np.zeros((oldHeight,oldWidth),np.int) #make a blank array for blue

    #Now get the specific channels. Remember: (B , G , R)
    red = (original[:,:,0]).astype('float')
    blue = (original[:,:,2]).astype('float')

    #Perform NDVI calculation
    summ = red+blue
    summ[summ<lowerLimit] = lowerLimit #do some saturation to prevent low intensity noise
    
    #ndvi is (1+NDVI)*127 so its range is 0 to 254 (but ndvi is an array object)
    ndvi = (((red-blue)/(summ)+1)*127).astype('uint8')  #the index
    
    redSat = (ndvi-128)*2  #red channel
    bluSat = ((255-ndvi)-128)*2 #blue channel
    redSat[ndvi<128] = 0 #if the NDVI is less than -0.13, no red info. Try set to 255
    bluSat[ndvi>128] = 0 #if the NDVI is equal to or more than -0.13, no blue info. Try set to 255.
    #print(str(type(redSat)))#I added this line when trying to evaluate stuff..
    
    """
    ndvi = (red-blue)/summ #ranges -1 to +1
    ndvi_pos = ndvi+1 #ranges 0 to 2
    ndvi_pos_col = (ndvi_pos*127).astype('uint8') #ranges 0 to 255 (or 254?); uint relates to an 8 digit coding of numbers, guess I
    redSat = ndvi_pos_col
    bluSat = 0
    """
    
    
    
    #And finally output the image. Remember: (B , G , R)
    #Red Channel
    ndviImage[:,:,2] = redSat

    #Blue Channel
    ndviImage[:,:,0] = bluSat

    #Green Channel
    ndviImage[:,:,1] = 255-(bluSat+redSat)

    return ndviImage

"""
im =Image.open('45468700464_3a5d8f4eed_o.jpg')
rval, frame = im.read()
height = im.get(3) #get height
width = im.get(4) #get width
"""
im=cv2.imread('/Users/lorenzotruffagiachet/Documents/astro_pi/edizione_20_21/eposat/eposat_data/photo_0001.jpg')
#rval, frame = im.read()
#height = im.get(3) #get height
#width = im.get(4) #get width
ndviImage = NDVICalc(im) #makes a BGR image
ndviImage_rgb = cv2.cvtColor(ndviImage, cv2.COLOR_BGR2RGB) #makes a RGB image
"""
cv2.imshow('first_try_image',im)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
plt.imshow(ndviImage) #shows the BGR image
#plt.imshow(ndviImage_rgb) #shows the RGB image
plt.show()


