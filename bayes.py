import sys
import random
import itertools
import numpy as np
import cv2 as cv


MAP_FILE = 'cape_python.png'

# search area variables. turple holds four points of the map.
SA1_CORNERS = (130,265,180,315)  #(UL-X, UL-Y, LR-X, LR-Y)
SA2_CORNERS = (80, 255, 130, 305) #(UL-X, UL-Y, LR-X, LR-Y)
SA3_CORNERS = (105,205,155, 255) #(UL-X, UL-Y, LR-X, LR-Y)

#defines search class
def search():
  