import numpy as np
import cv2 as cv

filename = 'tictactoe.png'
img = cv.imread(filename)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#gray = np.float32(gray)
#dst = cv.cornerHarris(gray, 2, 3, 0.04)

# result is dilated for marking corners
#dst = cv.dilate(dst, None)

# Threshold for optimal value
#img[dst>0.01*dst.max()] = [0,0,255]

sift = cv.SIFT_create()
kp = sift.detect(gray, None)

img = cv.drawKeypoints(gray, kp, img, flags=cv.DrawMatchesFlags_DRAW_RICH_KEYPOINTS)

cv.imwrite('sift_keypoints.jpg', img)

#cv.imshow('dst', img)
#if cv.waitKey(0) & 0xff == 27:
#    cv.destroyAllWindows()

## MAKE A FRICKING MASK OF THE IMAGE AND FIGURE IT OUT THAT WAY YOU DIMWIT
## then create a detection system for x's or o's (maybe both)