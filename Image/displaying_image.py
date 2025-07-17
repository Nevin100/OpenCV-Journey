import cv2

# Loading Of Image 
image = cv2.imread("./flower.jpeg")

if image is not None:
  # Displaying the image
  cv2.imshow('Flower Image', image) 
  
  # Wait for a key press
  cv2.waitKey(0) 
  
  # Close the image window
  cv2.destroyAllWindows()
  
else: 
  print('Error: Image Not Found')
  
  