import numpy as np
import cv2

def operation(image):
    kernel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    kernel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

    sobelX = np.zeros_like(image)
    sobelY = np.zeros_like(image)
    
    for y in range(1, image.shape[0] - 1):  #sobel kernels, excluding first and last rows and columns
        for x in range(1, image.shape[1] - 1):
            area = image[y-1:y+2, x-1:x+2] #operation area 3x3
            sobelX[y, x] = np.sum(area * kernel_x) #adds up 3x3 area with kernel multipliers
            sobelY[y, x] = np.sum(area * kernel_y)
            
    #combine x and y kernel     
    combinedXY = np.hypot(sobelX, sobelY)
            
    #find max value
    max_value = np.max(combinedXY)
                
    #normalize between 0-255
    combinedXY = (combinedXY / max_value) * 255
            
    #threshold = 128
    #combinedXY[combinedXY < threshold] = 0
    #combinedXY[combinedXY >= threshold] = 255
    
    return combinedXY 