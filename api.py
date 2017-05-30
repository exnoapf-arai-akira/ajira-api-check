#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import json
import urllib2
import os

f = open('urllist2.txt')

for url in f:
    list = url.split("/")
    filename = list[-1]
    print url
    cmd = "wget %s" % (url)
    os.system(cmd)

    img = cv2.imread(filename)

    aurl = 'http://52.38.2.70:5000/api/maria?url='+str(url)

    r = urllib2.urlopen(aurl)
    jsonData = json.loads(r.read())
    r.close()
    ##print json.dumps(jsonData, sort_keys=True, indent=4)

    for list in jsonData['detect']:
        cv2.rectangle(img,(list['right'],list['top']),(list['left'],list['bottom']),(0,255,0),3)
        cv2.putText(img,list['label'],(list['left'],list['top']-10),cv2.FONT_HERSHEY_SIMPLEX, 1,(0, 0, 255),2)

##cv2.imshow('result', img)
##cv2.waitKey(0)
##cv2.destroyAllWindows()

    cv2.imwrite("detect-"+filename, img)


f.close()
### right,top,left,bottom
