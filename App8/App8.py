import cv2

img = cv2.imread("E:\my_folder\python\Python_repo\App8\galaxy.jpg", 1)

resize_img = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))

cv2.imwrite("Galaxy_resized.jpg", resize_img)
cv2.imshow("Galaxy", resize_img)
cv2.waitKey(0)