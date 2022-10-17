import pytesseract
import cv2
import os
# from skimage import io
import numpy as np
from imutils import paths
from textblob import TextBlob
inputDir = 'input_image/'
outputDir = 'result/'
# imageName = list(filter(lambda file: file[-3:] == 'png', os.listdir(inputDir)))
imageName = list(paths.list_images(inputDir))


# def loadImage(imgPath):
#     img = cv2.imread(imgPath)
#     img = cv2.resize(img, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     kernel = np.ones((1, 1), np.uint8)
#     img = cv2.dilate(img, kernel, iterations=1)
#     img = cv2.erode(img, kernel, iterations=1)
#     cv2.threshold(cv2.GaussianBlur(img, (5, 5), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
#
#     cv2.threshold(cv2.bilateralFilter(img, 5, 75, 75), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
#
#     cv2.threshold(cv2.medianBlur(img, 3), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
#
#     cv2.adaptiveThreshold(cv2.GaussianBlur(img, (5, 5), 0), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31,
#                           2)
#
#     cv2.adaptiveThreshold(cv2.bilateralFilter(img, 9, 75, 75), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,
#                           31, 2)
#
#     cv2.adaptiveThreshold(cv2.medianBlur(img, 3), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
#     return img
#
#
# for imgPath in imageName:
#     print(imgPath)
#     img = loadImage(imgPath)
#
#     custom_oem_psm_config = '--oem 3 --psm 3'
#
#     with open(outputDir + imgPath[imgPath.rfind('/') + 1:-3] + 'txt', 'w', encoding='utf-8') as f:
#         f.write(pytesseract.image_to_string(img, lang='vie', config=custom_oem_psm_config))


# iterate over files in
# that directory
for filename in os.listdir(inputDir):
    f = os.path.join(inputDir, filename)
    os.system(r'tesseract '+ f +' stdout --oem 3 --psm 0')

for filename in os.listdir(inputDir):
    f = os.path.join(inputDir, filename)
    os.system('tesseract ' + f +' ' + outputDir+'/'+filename+' -l vie --oem 3 --psm 3')