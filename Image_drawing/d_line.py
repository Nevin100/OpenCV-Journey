# Drawing Line using openCV

# cv2.line(image, start_point, end_point, color, thickness) where image is the image on which you want to draw the line,
# start_point is the starting point of the line, end_point is the ending point of the line,
# color is the color of the line in BGR format, and thickness is the thickness of the line.

import cv2

# Create a blank image
image = cv2.imread('./flower.jpeg')

if image is None:
    print("Error: Could not read the image.")
else:
  print("Image loaded successfully.")
  
  # Define start and end points of the line
  start_point = (0, 0)  # Starting point (x, y)
  
  # Define end point of the line
  end_point = (60, 80)  # Ending point (x, y)
  
  # Define color in BGR format (blue, green, red)
  color = (255, 0, 0)  # Blue color
  
  # Define thickness of the line
  thickness = 2  # Thickness of the line
  
  # Draw the line on the image
  cv2.line(image, start_point, end_point, color, thickness)
  # Display the image with the drawn line
  cv2.imshow('Image with Line', image)
  cv2.waitKey(0)  # Wait for a key press to close the window
  cv2.destroyAllWindows()  # Close all OpenCV windows
  # Save the modified image
  cv2.imwrite('output_image_with_line.png', image)
  
  print("Line drawn and image saved as 'output_image_with_line.png'.")