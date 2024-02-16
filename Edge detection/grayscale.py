import numpy as np
import cv2

def operation(image):
    grayscale_image = np.zeros((image.shape[0],image.shape[1])) #create empty array for grayscale
    
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            grayscale_image[y, x] = np.clip(0.299*image[y, x, 2] + 0.587*image[y, x, 1] + 0.114*image[y, x, 0], 0, 255) #RGB, formula for grayscale
            
    return grayscale_image.astype(np.uint8) #8 bit integer