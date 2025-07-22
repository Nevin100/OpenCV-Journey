# Flipping Image using OpenCV

# Flipping can be done horizontally, vertically, or both using cv2.flip(image, flipCode) where flipCode:
# 0 means flipping around the x-axis (vertical flip),
# 1 means flipping around the y-axis (horizontal flip), and -1 means flipping around both axes.

import cv2

image = cv2.imread('./flower.jpeg')

if image is not None:
  flip_vertical = cv2.flip(image, 0)  # Vertical flip
  flip_horizontal = cv2.flip(image, 1)  # Horizontal flip
  flip_both = cv2.flip(image, -1)  # Flip both axes
  
  # Display the original and flipped images
  cv2.imshow('Original Image', image)
  cv2.imshow('Flipped Vertical', flip_vertical)
  cv2.imshow('Flipped Horizontal', flip_horizontal)
  
  cv2.imshow('Flipped Both', flip_both)
  cv2.imwrite('./flipped_vertical_flower.jpeg', flip_vertical)  # Save the vertically flipped image
  cv2.imwrite('./flipped_horizontal_flower.jpeg', flip_horizontal)  # Save the horizontally flipped image
  cv2.imwrite('./flipped_both_flower.jpeg', flip_both)  # Save the flipped both axes image
  
  cv2.waitKey(0)
  cv2.destroyAllWindows()
else:
    print("Error: Could not read the image. Please check the file path.")