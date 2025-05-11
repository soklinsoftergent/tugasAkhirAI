import cv2
import numpy as np
from PIL import Image

def intoGrayScale(pathToFile):
    """Convert image into grayscale and return the grayscaled image object"""
    image = cv2.imread(pathToFile)
    grayedImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # cv2.imwrite(pathToSave, grayedImage)
    return grayedImage

def intoBinary(pathToImage):
    """Convert image into binary"""
    

intoGrayScale('Pasted image.png')