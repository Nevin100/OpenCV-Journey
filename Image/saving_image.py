import cv2

image = cv2.imread("./flower.jpeg")

if image is not None:
  success = cv2.imwrite("Output_python.png", image)
  
  if success:
    print("Image Saved Successfully")
    
  else:
    print("Error: Image Not Saved")
    
else:
  print('Error: image could not be loaded')
  