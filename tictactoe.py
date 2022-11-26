import numpy as np
import cv2 as cv

img = np.zeros((512,512), np.uint8)

cv.line(img, (170,0), (170,512), (255,255,255), 5)
cv.line(img, (340,0), (340,512), (255,255,255), 5)
cv.line(img, (0,170), (512,170), (255,255,255), 5)
cv.line(img, (0,340), (512,340), (255,255,255), 5)

cv.imshow("Testing", img)
k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("tictactoe.png", img)