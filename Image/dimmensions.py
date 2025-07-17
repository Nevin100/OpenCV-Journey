import cv2

image = cv2.imread('./flower.jpeg')

if image is not None:
  # Get the dimensions of the image
  # h = height, w = width, c = color channels
  h,w,c = image.shape
  print(f"Image dimensions: {h} x {w} pxs with {c} color channels")
  
else:
  print("Error: Image not found or could not be read.")