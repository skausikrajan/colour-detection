import numpy as np
import cv2
print(" please select the colours from this \n 1) red \n 2) white \n 3) gray \n 4) blue \n 5) orange \n 6) yellow \n 7) violet \n 8) green \n 9) brown \n 10) black \n 11) pink \n 12)light blue \n 13) purple \n 14) light green \n 15) gold")
colour=input("enter the colour name:")
#Defining RGB Colour values
if 'red' in colour:
 a=0
 b=0
 c=255
elif 'white' in colour:
 a=255
 b=255
 c=255
elif 'gray' in colour:
 a=128
 b=128
 c=128
elif 'blue' in colour:
 a=0
 b=0
 c=255
elif "light blue" in colour:
 a=0
 b=191
 c=255
elif 'orange' in colour:
 a=255
 b=165
 c=0
elif "yellow" in colour:
 a=255
 b=255
 c=0
elif "violet" in colour:
 a=238
 b=130
 c=238
elif "green" in colour:
 a=0
 b=128
 c=0
elif "brown" in colour:
 a=165
 b=42
 c=42
elif "black" in colour:
 a=0
 b=0
 c=0
elif "pink" in colour:
 a=255
 b=192
 c=203
elif "purple" in colour:
 a=128
 b=0
 c=128
elif "light green" in colour:
 a=154
 b=205
 c=50
elif "gold" in colour:
 a=255
 b=215
 c=0
else:
 a=0
 b=0
 c=0
# Capturing video through webcam
webcam = cv2.VideoCapture(0)

# Start a while loop
while(1):
	
	# Reading the video from the
	# webcam in image frames
	_, imageFrame = webcam.read()

	# Convert the imageFrame in
	# BGR(RGB color space) to
	# HSV(hue-saturation-value)
	# color space
	hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)

	# Set range for red color and
	# define mask
	red_lower = np.array([136, 87, 111], np.uint8)
	red_upper = np.array([180, 255, 255], np.uint8)
	red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)

	
	# Morphological Transform, Dilation
	# for each color and bitwise_and operator
	# between imageFrame and mask determines
	# to detect only that particular color
	kernal = np.ones((5, 5), "uint8")
	
	# For red color
	red_mask = cv2.dilate(red_mask, kernal)
	res_red = cv2.bitwise_and(imageFrame, imageFrame,
							mask = red_mask)

	# Creating contour to track red color
	contours, hierarchy = cv2.findContours(red_mask,
										cv2.RETR_TREE,
										cv2.CHAIN_APPROX_SIMPLE)
	
	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area > 300):
			x, y, w, h = cv2.boundingRect(contour)
			imageFrame = cv2.rectangle(imageFrame, (x, y),
									(x + w, y + h),
									(a,b,c), 2)
			
			cv2.putText(imageFrame, "COLOUR DETECTED", (x, y),
						cv2.FONT_HERSHEY_SIMPLEX, 1.0,
						(a,b,c))	
	# Program Termination
	cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame)
	if cv2.waitKey(10) & 0xFF == ord('q'):
		cap.release()
		cv2.destroyAllWindows()
		break
