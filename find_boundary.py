import cv2 as cv
import numpy as np

img = cv.cvtColor(cv.imread("./imgs/box-2.jpeg"), cv.COLOR_BGR2RGB)

r = cv.selectROI("select the area", img)  # top left + bottom right coordiantes


mask = np.zeros(img.shape[:2], np.uint8)
background = np.zeros((1, 65), np.float64)
foreground = np.zeros((1, 65), np.float64)

# Run GrabCut to segment the object
cv.grabCut(img, mask, r, background, foreground, 5, cv.GC_INIT_WITH_RECT)

# Create a mask with the foreground pixels (1) and probable foreground pixels (3)
mask2 = np.where((mask == 1) + (mask == 3), 255, 0).astype("uint8")

# plt.imshow(mask2,cmap='gray')
cv.waitKey(0)
cv.destroyAllWindows()

# ---------Finding Contour-----------
flipped = cv.flip(mask2, 0)
contours1, hierarchy1 = cv.findContours(
    flipped, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE
)
# print(contours1)

# print(contours1)
# imgCopy=cv.cvtColor(cv.imread('test0.png'), cv.COLOR_BGR2RGB)
cv.drawContours(img, contours1, -1, (0, 0, 255), 1)

cv.imwrite("contour.png", img)
top_face_coordinates = contours1
sumX, sumY = 0, 0
for coordinate in top_face_coordinates:
    for pt in coordinate:
        for x, y in pt:
            sumX += x
            sumY += y
            # print(x, y)

# # Calculate the average of x and y coordinates
center_x = sumX / len(top_face_coordinates[0])
center_y = sumY / len(top_face_coordinates[0])

# The center of the top face, (also the travel distance)
center_top_face = (center_x, center_y)
print(len(top_face_coordinates[0]))
print(center_top_face)
