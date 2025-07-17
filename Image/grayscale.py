import cv2

image = cv2.imread('./flower.jpeg')

if image is not None:
    # image is loaded successfully and image is being converted to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    if gray_image is not None:
      
        # showing the grayscale image
        cv2.imshow('Gray Scale Image', gray_image)
      
        cv2.waitKey(0)
        
        cv2.destroyAllWindows()
        
        cv2.imwrite('./flower_gray.jpeg', gray_image)
        print("Image converted to grayscale and saved as 'flower_gray.jpeg'.")
    else:
        print("Error: Could not convert image to grayscale.")
        
else:
    print("Error: Could not load image.")
    
    