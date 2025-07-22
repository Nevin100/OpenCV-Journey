# Adding Text to an Image using OpenCV

# cv2.putText(image, text, org, font, font_scale, color, thickness) where
# text: The text to be added
# org: Bottom-left corner of the text string in the image
# font: Font type (e.g., cv2.FONT_HERSHEY_SIMPLEX)
# font_scale: Font scale factor that is multiplied by the font-specific base size
# color: Color of the text in BGR format

import cv2

image = cv2.imread('./flower.jpeg')

if image is None:
    print("Error: Could not read the image.")
    
else:
    text = "Hello"
    org = (50, 50)  # Bottom-left corner of the text
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    color = (255, 255, 255)  # White color in BGR
    thickness = 2
    
    # Add text to the image
    cv2.putText(image, text, org, font, font_scale, color, thickness)
    
    # Display the image with the text
    cv2.imshow('Image with Text', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    # Save the modified image
    cv2.imwrite('./flower_with_text.jpeg', image)
    print("Image saved as 'flower_with_text.jpeg'.")