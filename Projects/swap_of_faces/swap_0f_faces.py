import cv2
import dlib
import numpy as np

# Initialize dlib's face detector and landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")  # Download from dlib model zoo

def get_landmarks(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    if len(faces) == 0:
        raise Exception("No face detected")
    return np.matrix([[p.x, p.y] for p in predictor(gray, faces[0]).parts()])

def transformation_matrix(from_points, to_points):
    return cv2.estimateAffinePartial2D(from_points, to_points)[0]

def warp_image(src, M, shape):
    output = np.zeros(shape, dtype=src.dtype)
    cv2.warpAffine(src, M, (shape[1], shape[0]), dst=output, borderMode=cv2.BORDER_TRANSPARENT)
    return output

def swap_faces(img1, img2):
    landmarks1 = get_landmarks(img1)
    landmarks2 = get_landmarks(img2)

    M = transformation_matrix(landmarks1, landmarks2)

    warped_face = warp_image(img1, M, img2.shape)
    mask = np.ones_like(warped_face, dtype=np.uint8) * 255

    center = (img2.shape[1] // 2, img2.shape[0] // 2)
    output = cv2.seamlessClone(warped_face, img2, mask, center, cv2.NORMAL_CLONE)
    return output

# Load your images
image1 = cv2.imread("face1.jpg")
image2 = cv2.imread("face2.jpg")

result = swap_faces(image1, image2)

# Show or save result
cv2.imshow("Face Swapped", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
