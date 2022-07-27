from imutils.perspective import four_point_transform
from imutils import contours
import imutils
import pytesseract as pytesseract
import pytesseract
import cv2

filename = "C:\\Users\\Pramod M\\Documents\\frame28.jpg"
#cv2.IMREAD_COLOR = 1 , Loads a color image. Any transparency of image will be neglected. It is the default flag.
#cv2.IMREAD_GRAYSCALE = 0 , Loads image in grayscale mode
#cv2.IMREAD_UNCHANGED = -1 , Loads image as such including alpha channel
image = cv2.imread( filename , 1 )

image = imutils.resize(image, height=500)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(blurred, 50, 200, 255  )

cv2.imwrite( 'res.png', edged )
cv2.imshow('result', edged)
cv2.waitKey()

image = cv2.imread(filename, 0)

custom_config = '--psm 6'
txt = pytesseract.image_to_string(edged, config=custom_config)
print(txt)
file = open("recognized.txt", "a")
file.write(txt)
# Close the file
file.close()