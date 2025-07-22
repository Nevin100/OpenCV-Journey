# Drawing Rectangle using openCV

# cv2.rectangle(image, start_point, end_point, color, thickness) where
# start_point: Top-left corner of the rectangle
# end_point: Bottom-right corner of the rectangle

import cv2 

image = cv2.imread('./flower.jpeg')

if image is None:
    print("Error: Could not read the image.")
else:
    start_point = (50, 50)
    end_point = (200, 200)
    
    color = (0, 255, 0)  # Green color in BGR
    thickness = 2  # Thickness of the rectangle border
    
    # Draw the rectangle on the image
    cv2.rectangle(image, start_point, end_point, color, thickness)
    # Display the image with the rectangle
    cv2.imshow('Image with Rectangle', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
# Save the modified image
    cv2.imwrite('./flower_with_rectangle.jpeg', image)
    print("Image saved as 'flower_with_rectangle.jpeg'.")
    