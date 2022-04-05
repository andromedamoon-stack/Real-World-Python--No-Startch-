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
class search():
  "Bayesian search & rescue game."
  def __init__(self,name):
    self.name = name
    self.img = cv.imread(MAP_FILE, cv.IMREAD_COLOR)
    if self.img is None:
      print('Could not load map file {}'.format(MAP_FILE), file=sys.stderr)
      sys.exit(1)]

    self.area_actual = 0
    self.sailor_actual = [0, 0] # local cord within search area

    self.sa1 = self.img[SA1_CORNERS[1] : SA1_CORNERS[3], SA1_CORNERS[0] : SA1_CORNERS[2]]

    self.sa2 = self.img[SA2_CORNERS[1] : SA2_CORNERS[3], SA2_CORNERS[0] : SA2_CORNERS[2]]

    self.sa3 = self.img[SA3_CORNERS[1] : SA3_CORNERS[3], SA3_CORNERS[0] : SA3_CORNERS[2]]

    self.p1 = 0.2
    self.p2 = 0.5
    self.p3 = 0.3

    self.sept1 = 0
    self.sept2 = 0
    self.sept3 = 0
  def draw_map(self,last_known):
    #Display basemap with scale, last known xy location, search areas
   
    cv.line(self.img,(20,370),(70,370),(0,0,0), 2)
    cv.putText(self.img, '0', (8, 370), cv.FONT_HERSHEY_PLAIN, 1,(0,0,0))
    cv.putText(self.img, '50 Nautical Miles', (71,370),cv.FONT_HERSHEY_PLAIN, 1, (0,0,0))

    # passes the base image, the vars, then a color turple
    cv.rectangle(self.img,(SA1_CORNERS[0], SA1_CORNERS[1]), (SA1_CORNERS[2], SA1_CORNERS[3]), (0,0,0), 1)
    cv.putText(self.img, '1', (SA1_CORNERS[0]+ 3, SA1_CORNERS[1] + 15), cv.FONT_HERSHEY_PLAIN, 1, 0)
    cv.rectangle(self.img, (SA2_CORNERS[0], SA2_CORNERS[1]),(SA2_CORNERS[2], SA2_CORNERS[3], (0,0,0), 1)
    cv.putText(self.img, '2', (SA2_CORNERS[0] + 3, SA2_CORNERS[1] + 15), CV.FONT_HERSHEY_PLAIN, 1, 0)
    cv.rectangle(self.img,(SA3_CORNERS[0], SA3_CORNERS[1]),(SA3_CORNERS[2], SA3_CORNERS[3]), (0,0,0),1)
    cv.putText(self.img, '3', (SA3_CORNERS[0] + 3, SA3_CORNERS[1] + 15), cv.FONT_HERSHEY_PLAIN, 1, 0)

    #2 posts a + at last known position
    cv.putText(self.img, '+', (last_known), cv.FONT_HERSHEY_PLAIN, 1, (0,0, 255))
    cv.putText(self.img, '+= Last Known Position', (274,355),cv.FONT_HERSHEY_PLAIN,1,(0,0,255))
    
  #3 show basemap using opencv imshow()
    cv.imshow('Search Area', self.img)
    cv.moveWIndow('Search Area', 750, 10)
    cv.waitKey(500)

    
  def sailor_final_location(self,num_search_areas):
    # method to randomly choose salior's location
    # find sailor coordinates with any search area sub array
    self.sailor_actual[0] = np.random.choice(self.sa1.shape[1], 1)
    self.sailor_actual[1] = np.random.choice(self.sa1.shape[0], 1)

    area = int(random.triangular(1, num_search_areas + 1))

    if area == 1:
      x = self.sailor[0] + SA1_CORNERS[0]
      y = self.sailor[1] + SA1_CORNERS[1]
      self.area_actual = 1

    elif area == 2:
      x = self.sailor[0] + SA2_CORNERS[0]
      y = self.sailor[1] + SA2_CORNERS[1]
      self.area_actual = 2

    elif area == 3:
      x = self.sailor[0] + SA3_CORNERS[0]
      y = self.sailor[1] + SA3_CORNERS[1]
      self.area_actual = 3
    return x, y

