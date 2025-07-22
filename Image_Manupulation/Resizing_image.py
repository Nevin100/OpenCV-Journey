# Resizing Image using resize()

# syntax : cv2.resize(src, dsize[, dst[, fx[, fy[, interpolation]]]])
# dsize : Desired size for the output image. If both fx and fy are specified, dsize is ignored.
# interpolation : Interpolation method used for resizing. Common methods include:
# cv2.INTER_LINEAR, cv2.INTER_NEAREST, cv2.INTER_CUBIC,

import cv2

image = cv2.imread('./flower.jpeg')

if image is None:
    print("Error: Could not read the image.")
    
else:
    # Resize the image to 300x300 pixels where the width and height are both set to 300 pixels (w x h)
    resized_image = cv2.resize(image, (400, 400))

    # Display the original and resized images
    cv2.imshow('Original Image', image)
    cv2.imshow('Resized Image', resized_image)

    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows() 