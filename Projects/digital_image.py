import cv2
from PIL import Image

# Start the webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Cannot open camera")
    exit()

# Read one frame
ret, frame = cap.read()

if ret:
    # Save using OpenCV
    cv2.imwrite("clicked_photo.jpg", frame)
    print("✅ Photo captured and saved as clicked_photo.jpg")

    # Optional: Open with Pillow and show it
    img = Image.open("clicked_photo.jpg")
    img.show()

else:
    print("❌ Failed to capture image")

cap.release()



