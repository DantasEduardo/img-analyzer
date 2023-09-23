import cv2
import numpy as np


def main(img_path:str) -> float:
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    # noise removal
    kernel = np.ones((3,3),np.uint8)
    opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)

    sure_bg = cv2.dilate(opening,kernel,iterations=3)

    percentage = (np.count_nonzero(sure_bg == 0) * 100)/(sure_bg.shape[0] * sure_bg.shape[1])

    return round(percentage, 2)


if __name__ =='__main__':
    path = 'data\img_slice.png'
    main(path)