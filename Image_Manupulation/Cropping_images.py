# Cropping of images using slices :

# cropped_image = image[startY:endY, startX:endX]

import cv2

# Load the image
image = cv2.imread('./flower.jpeg')

if image is not None :
  cropped_image = image[10:, 20:]  # Adjust the slice values as needed
  
  cv2.imshow('Cropped Image', cropped_image)
  
  cv2.waitKey(0)  # Wait for a key press to close the window
  cv2.destroyAllWindows()  # Close all OpenCV windows
else:
  print("Error: Image not found or could not be loaded.")