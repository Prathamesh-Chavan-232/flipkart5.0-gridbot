import cv2 as cv
import numpy as np

img = cv.cvtColor(cv.imread('box-2.jpeg'), cv.COLOR_BGR2RGB)

r = cv.selectROI("select the area", img)  # top left + bottom right coordiantes


mask = np.zeros(img.shape[:2], np.uint8)
background = np.zeros((1, 65), np.float64)
foreground = np.zeros((1, 65), np.float64)

# Run GrabCut to segment the object
cv.grabCut(img, mask, r, background, foreground, 5, cv.GC_INIT_WITH_RECT)

# Create a mask with the foreground pixels (1) and probable foreground pixels (3)
mask2 = np.where((mask == 1) + (mask == 3), 255, 0).astype('uint8')

# plt.imshow(mask2,cmap='gray')
cv.waitKey(0)
cv.destroyAllWindows()

# ---------Finding Contour-----------
flipped = cv.flip(mask2, 0)
contours1, hierarchy1 = cv.findContours(
    flipped, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
print(contours1)

# print(contours1)
# imgCopy=cv.cvtColor(cv.imread('test0.png'), cv.COLOR_BGR2RGB)
cv.drawContours(img, contours1, -1, (0, 0, 255), 1)

cv.imwrite('contour.png', img)
top_face_coordinates = contours1

# Calculate the average of x and y coordinates
center_x = sum(x for x, y in top_face_coordinates) / len(top_face_coordinates)
center_y = sum(y for x, y in top_face_coordinates) / len(top_face_coordinates)

# The center of the top face
center_top_face = (center_x, center_y)
