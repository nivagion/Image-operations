import numpy as np
import cv2

import sobel
import grayscale

whatToDo = input("single char: sobel-so  greyscale-gs : ")

image = cv2.imread('input/Happi.png')

if whatToDo == 'so':
    grayscale_image = grayscale.operation(image)
    sobel_image = sobel.operation(grayscale_image) #needs grayscale to work
    #save it
    cv2.imwrite('output/output.jpg', sobel_image)
    #display it
    #cv2.imshow('sobel', sobel_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

elif whatToDo == 'gs':
    grayscale_image = grayscale.operation(image)
    #save it
    cv2.imwrite('output/output.jpg', grayscale_image)
    #display it
    #cv2.imshow('grayscale', grayscale_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

