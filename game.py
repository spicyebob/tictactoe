import tictactoe as t
import cv2 as cv

m = t.setup()
print(m)

ready = input("Ready? y/n")
if ready == 'n':
    reset = input("reset? y/n")
    if reset == 'y':
        t.reset()

try:
    if ready == 'y':
        mask = m != 0
        n = m[mask]
        while len(n) > 0:
            advance = input("Advance? y/n")
            try:
                if advance == 'y':
                    a = t.detect(m)
                    m = a[1]
                    print(m)
                    b = t.next_move(a[0],a[1])
                    m = b[1]
                    print(m)
                    mask = b[1] != 0
                    n = b[1][mask]
                    print(len(n))
                else:
                    break
            except:
                break
except:
    print("please try again")


#a = t.detect(m)
#print(a[0])
#print(a)
#img = a[0]
#print(a[1])
#cv.imshow("test 3", img)
#k = cv.waitKey(0)
#if k == ord('s'):
#    cv.destroyAllWindows()

#b = t.next_move(a[0], a[1])

#img = b[0]
#print(b[1])
#cv.imshow("test 4", img)
#k = cv.waitKey(0)
#if k == ord('s'):
#    cv.destroyAllWindows()

#mask = m != 0
#n = m[mask]
#while len(n) > 0:
#    advance = input("Advance? y/n")
#    a = t.detect(m)
#    b = t.next_move(a[0],a[1])
#    mask = b[1] != 0
#    n = b[1][mask]