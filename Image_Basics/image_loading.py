import cv2

# Loading Of Image 
image = cv2.imread("./flower.jpeg")

if image is not None:
  print('Image Loaded Successfully')
  
else: 
  print('Error: Image Not Found')
  
  