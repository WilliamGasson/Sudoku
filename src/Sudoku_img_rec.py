import cv2
import numpy as np
import random as rng
from matplotlib import pyplot as plt
import imutils 
import easyocr


class image_identifier():

    def __init__(self):
        self.img = []
        self.img_grey = []
        self.contours = []
        self.threshold = 100

    def loadImg(self, image_file=None):
        # Load image
        if image_file == None:
            image_file = 'img\sudoku2.png'

        img = cv2.imread(cv2.samples.findFile(image_file))
        if img is None:
            print('Could not open or find the image:', image_file)
            exit(0)
        # Pre- process
        size = 900
        img_resize = cv2.resize(img, (size,size), interpolation = cv2.INTER_AREA)
        self.img_gray = cv2.cvtColor(img_resize, cv2.COLOR_BGR2GRAY)
        #self.img_gray = cv2.blur(self.img_gray, (3,3))
        plt.imshow(self.img_gray)


    def findBoxes(self):
        # Find Bounding contours
        canny_output = cv2.Canny(self.img_gray, self.threshold, self.threshold * 2)
        keypoints = cv2.findContours(canny_output.copy(), cv2.RETR_LIST , cv2.CHAIN_APPROX_SIMPLE)
        self.contours = imutils.grab_contours(keypoints) # grab contours
        #contours = sorted(contours, key= cv2.contourArea, reverse=True)[:180] # grab the 10 biggest contours



        drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)
        boundRect = []
        for i, contour in enumerate(self.contours):
            if cv2.contourArea(contour) < 10500 and cv2.contourArea(contour) >9000 :
                #print(cv2.contourArea(contour))
                boundRect = cv2.boundingRect(contour)
                color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))
                rectangles = cv2.rectangle(drawing, (int(boundRect[0]), int(boundRect[1])),(int(boundRect[0]+boundRect[2]), int(boundRect[1]+boundRect[3])), color, 2)

        plt.imshow(drawing)



    def idNumbers(self):
        sudokuBoard = np.zeros((9, 9))
        counter = 0
        for i, contour in enumerate(self.contours):
            if cv2.contourArea(contour) < 10500 and cv2.contourArea(contour) >9000:
                approx = cv2.approxPolyDP(contour, 4, True) # approximate to see if it is square
                mask = np.zeros(self.img_gray.shape,np.uint8)    # blank mask
                new_image = cv2.drawContours(mask, [approx], 0,255, -1) 
                new_image = cv2.bitwise_and(self.img_gray,self.img_gray, mask = mask)

                x,y = np.where(mask == 255)
                x1,y1 = np.min(x), np.min(y)
                x2,y2 = np.max(x), np.max(y)
                cropped_image = self.img_gray[x1:x2+1,y1:y2+1]

                
                # if new_image canney is not empty
                canny_mask = cv2.Canny(cropped_image[10:len(cropped_image)-10, 10:len(cropped_image)-10], self.threshold, self.threshold * 2)


                if not np.all((canny_mask == 0)):
                    reader = easyocr.Reader(['en'])
                    result = reader.readtext(cropped_image)
                    print(result)
                    
                    if result != []:
                        boxX = int((x1+x2)/(2*100))
                        boxY = int((y1+y2)/(2*100))
                        boxV = result[0][1]
                        sudokuBoard[boxX,boxY] = boxV


        print(sudokuBoard)
        plt.show()
        return sudokuBoard

