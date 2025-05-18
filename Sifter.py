import cv2
import numpy as np
from PIL import Image
np.set_printoptions(threshold=np.inf)

def intoGrayScale(pathToFile):
    """Convert image into grayscale and return the grayscaled image object"""
    image = cv2.imread(pathToFile)
    grayedImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # cv2.imwrite(pathToSave, grayedImage)
    return grayedImage

def intoBinary(pathToImage):
    """Convert image into binary"""
    

def asArray(pathToImage, pathToSave="pixelValues.txt"):
    image = cv2.imread(pathToImage)
    convertRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    with open(pathToSave, "a") as f:
        for line in convertRGB:
            f.write(str(line))
    return
# intoGrayScale('Pasted image.png')
print(asArray('newIm.png'))