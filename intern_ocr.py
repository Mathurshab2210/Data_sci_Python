# -*- coding: utf-8 -*-
"""intern_ocr.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Pv9qeUe2OrFV34gJDGHGqMFvx18PdhFc
"""

!pip install easyocr

import matplotlib.pyplot as plt
import cv2
import easyocr
from pylab import rcParams
from IPython.display import Image
rcParams['figure.figsize'] = 8, 16

reader = easyocr.Reader(['en'])

Image("trial1.jpg")

output = reader.readtext("c")

output

cord = output[-1][0]

x_min, y_min = [int(min(idx)) for idx in zip(*cord)]

x_max, y_max = [int(max(idx)) for idx in zip(*cord)]

image = cv2.imread('/trial1.jpg')
cv2.rectangle(image,(x_min,y_min),(x_max,y_max),(0,0,255),2)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))