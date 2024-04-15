import cv2
import numpy as np 

# Load image
image = cv2.imread('shapes.jpg')

# Convert image to HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Ask user for commit
filter_color = input("Enter filter color: ")

# Initialize BGR color values
# red
if filter_color == 'red': 
    color = np.uint8([[[0, 0, 255]]]) 
# orange
elif filter_color == 'orange':
    color = np.uint8([[[0, 127, 255]]]) 
# yellow
elif filter_color == 'yellow':
    color = np.uint8([[[0, 255, 255]]]) 
# green
elif filter_color == 'green':
    color = np.uint8([[[0, 255, 0]]]) 
# blue
elif filter_color == 'blue':
    color = np.uint8([[[255, 0, 0]]]) 
# indigo
elif filter_color == 'indigo':
    color = np.uint8([[[130, 0, 75]]]) 
# violet
elif filter_color == 'violet':
    color = np.uint8([[[211, 0, 148]]]) 

# Get hue value of user's chosen color
hsv_color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)

# Initialize mask by creating lower and upper range for colors
hue = hsv_color[0][0][0]
lower = np.array([hue - 10, 100, 100])
upper = np.array([hue + 10, 255, 255])

# Apply mask to image
masked_image = cv2.inRange(hsv_image, lower, upper) 

# Show Image
cv2.imshow('Original Image', image)
cv2.imshow('HSV Image', masked_image)

# Wait for a key press and then close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()