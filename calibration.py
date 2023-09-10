import numpy as np
import cv2
import glob

pattern_size = (9, 6)  # Number of inner corners (rows, columns)


def find_corners(image):
    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    success, corners = cv2.findChessboardCorners(gray, pattern_size, None)
    return success, corners, gray


def calibrate_camera(calibration_images):
    object_points = []  # 3D points in real-world coordinates
    image_points = []   # 2D points in image coordinates

    # Create a grid of 3D points corresponding to the calibration pattern
    objp = np.zeros((np.prod(pattern_size), 3), np.float32)
    objp[:, :2] = np.mgrid[0:pattern_size[0],
                           0:pattern_size[1]].T.reshape(-1, 2)

    for image in calibration_images:
        success, corners, gray = find_corners(image)
        if success:
            object_points.append(objp)
            image_points.append(corners)

    # Perform camera calibration
    ret, camera_matrix, dist_coeffs, rvecs, tvecs = cv2.calibrateCamera(
        object_points, image_points, gray.shape[::-1], None, None)

    return ret, camera_matrix, dist_coeffs


# List of calibration images
calibration_images = glob.glob('./Calib_Imgs/*.jpg')
ret, camera_matrix, dist_coeffs = calibrate_camera(calibration_images)

if ret:
    print("Camera calibration successful.")
else:
    print("Camera calibration failed.")

# Save calibration data
np.savetxt('camera_matrix.txt', camera_matrix)
np.savetxt('dist_coeffs.txt', dist_coeffs)
