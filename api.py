#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import json
import urllib2
import os
import urllib


def url_to_image(url):
	resp = urllib.urlopen(url)
	image = np.asarray(bytearray(resp.read()), dtype="uint8")
	image = cv2.imdecode(image, cv2.IMREAD_COLOR)
	return image

urls = open('urllist2.txt')

#for url in f:
#    print url
#    urllist = url.split("/")
#    filename = urllist[-1]
#    cmd = "wget -N %s" % (url)
#    os.system(cmd)


for url in urls:
    urllist = url.split("/")
    filename = urllist[-1]
    print "downloading %s" % (url)
    img = url_to_image(url)

    aurl = 'http://52.38.2.70:5000/api/maria?url='+str(url)

    r = urllib2.urlopen(aurl)
    jsonData = json.loads(r.read())
    r.close()
    print json.dumps(jsonData, sort_keys=True, indent=4)

    #img = cv2.imread(filename)

    for list in jsonData['detect']:
        cv2.rectangle(img,(list['right'],list['top']),(list['left'],list['bottom']),(0,255,0),3)
        cv2.putText(img,list['label'],(list['left'],list['top']-10),cv2.FONT_HERSHEY_SIMPLEX, 1,(0, 0, 255),2)

    #cv2.imshow('result', img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    cv2.imwrite("detect-"+filename, img)


urls.close()
### right,top,left,bottom
