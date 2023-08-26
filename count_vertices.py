
import cv2
import numpy as np

# Load the image
image = cv2.imread('box-2.jpeg')

# Define the rectangle around the polygon (adjust coordinates as needed)
# rect = (x1, y1, x2, y2)
rect = []

# Create a mask
mask = np.zeros(image.shape[:2], np.uint8)

# Initialize background and foreground models
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

# Apply GrabCut algorithm
cv2.grabCut(image, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

# Modify the mask to make it binary (either foreground or background)
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

# Find contours in the mask
contours, _ = cv2.findContours(
    mask2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Get the largest contour (assuming it's the polygon)
largest_contour = max(contours, key=cv2.contourArea)

# Calculate the number of vertices
num_vertices = len(largest_contour)

print("Number of Vertices:", num_vertices)

# Draw the largest contour on the original image
image_with_contour = cv2.drawContours(
    image.copy(), [largest_contour], -1, (0, 255, 0), 2)

# Display the image with the detected contour
cv2.imshow('Image with Contour', image_with_contour)
cv2.waitKey(0)
cv2.destroyAllWindows()
