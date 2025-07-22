# Drawing circle using openCV

# cv2.circle(image, center, radius, color, thickness) where
# center: Center of the circle
# radius: Radius of the circle
import cv2

image = cv2.imread('./flower.jpeg')

if image is None:
    print("Error: Could not read the image.")
    
else:
    center = (20, 20)
    radius = 50
    color = (255, 0, 0)  # Blue color in BGR
    thickness = 2
    
    # Draw the circle on the image
    cv2.circle(image, center, radius, color, thickness)
    # Display the image with the circle
    cv2.imshow('Image with Circle', image)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    # Save the modified image
    cv2.imwrite('./flower_with_circle.jpeg', image)
    print("Image saved as 'flower_with_circle.jpeg'.")