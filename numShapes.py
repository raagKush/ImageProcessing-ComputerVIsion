import cv2
import numpy as np

img = cv2.imread(r"Count-The-Number-of-Shapes.jpg")

img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
binary = cv2.adaptiveThreshold(img_grey, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV,5,6)

contours,hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(imgCopy, contours, -1, (0,255,0))
# cv2.imshow('img', imgCopy)
cnt_rect = 0
cnt_tri =0
cnt_circ = 0

for cnt in contours:
    area = cv2.contourArea(cnt)
    if area<200:
        continue
        
    else:
        epsilon = 0.01*cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)
        
        #circle
        (x,y),radius = cv2.minEnclosingCircle(cnt)
        circleArea = np.pi*radius*radius
        circularity = area/circleArea
        
        if len(approx)==4:
            print("rectangle")
            cv2.drawContours(img, [cnt], -1, (0,255,0))
            cnt_rect +=1
            
        elif len(approx) == 3:
            print("triangle")
            cv2.drawContours(img, [cnt], -1, (255,0,0))
            cnt_tri +=1
            
        elif len(approx>6) and (0.75<circularity<1.25):
            print("circle")
            cv2.drawContours(img, [cnt], -1, (0,0,255))
            cnt_circ +=1
        
            
print("Num rect = ",cnt_rect)
print("Num_tri =", cnt_tri)
print("Num_circ = ",cnt_circ)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
