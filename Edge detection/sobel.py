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
    combinedXY = np.zeros_like(image)
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            combinedXY[y, x] = np.sqrt(sobelX[y, x]**2 + sobelY[y, x]**2)
            #combinedXY[y, x] = sobelY[y, x]
    #find max value
    max_value = combinedXY[0, 0]
    for y in range(combinedXY.shape[0]):
        for x in range(combinedXY.shape[1]):
            if combinedXY[y, x] > max_value:
                max_value = combinedXY[y, x]
                
    #use max value to normalize between 0-255
    for y in range(combinedXY.shape[0]):
        for x in range(combinedXY.shape[1]):
            combinedXY[y, x] = (combinedXY[y, x] / max_value) * 255
            
    threshold = 128
    combinedXY[combinedXY < threshold] = 0
    combinedXY[combinedXY >= threshold] = 255
    
    return combinedXY.astype(np.uint8) #8 bit integer