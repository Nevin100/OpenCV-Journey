# Rotation of Images using OpenCV

# M = cv2.getRotationMatrix2D(center, angle, scale) where angle is in degrees and scale is the scaling factor
# rotated_image = cv2.warpAffine(image, M, (width, height)) where image is the original image, M is the rotation matrix, and (width, height) is the size of the output image

import cv2

image = cv2.imread('./flower.jpeg')

if image is not None:
    # Get the dimensions of the image
    height, width = image.shape[:2]

    # Define the center of the image for rotation
    center = (width // 2, height // 2)

    # Define the rotation angle and scale
    angle = 45  # Rotate by 45 degrees
    scale = 0.4  # scaling is set to 0.4

    # Get the rotation matrix
    M = cv2.getRotationMatrix2D(center, angle, scale)

    # Perform the rotation
    rotated_image = cv2.warpAffine(image, M, (width, height))

    # Display the original and rotated images
    cv2.imshow('Original Image', image)
    cv2.imshow('Rotated Image', rotated_image)
    
    cv2.imwrite('./rotated_flower.jpeg', rotated_image)  # Save the rotated image
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
else:
    print("Error: Could not read the image. Please check the file path.")