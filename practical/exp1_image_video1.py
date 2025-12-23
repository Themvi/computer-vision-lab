import cv2
import os

img_path = r"D:\mtech\image.jpg"


if not os.path.exists(img_path):
    print("Error: Image file not found!")
else:
    img = cv2.imread(img_path, cv2.IMREAD_COLOR)
    gray = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    if img is None or gray is None:
        print("Error: Image could not be loaded!")
    else:
        cv2.imshow("Color Image", img)
        cv2.imshow("Gray Image", gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()