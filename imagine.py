import os
import numpy as np
from matplotlib import pyplot as plt
from geoip import geolite2
from urllib2 import urlopen
from openalpr import Alpr
import sys
import cv2
from glob import glob
import itertools as it
import urllib
import urllib2
import requests
import matplotlib as mpl

host = 'http://localhost'
port = '5000'
url = host + ':' + port

def inside(r, q):
    rx, ry, rw, rh = r
    qx, qy, qw, qh = q
    return rx > qx and ry > qy and rx + rw < qx + qw and ry + rh < qy + qh

def draw_detections(img, rects, thickness = 1):
    for x, y, w, h in rects:
        # the HOG detector returns slightly larger rectangles than the real objects.
        # so we slightly shrink the rectangles to get a nicer output.
        pad_w, pad_h = int(0.15*w), int(0.05*h)
        cv2.rectangle(img, (x+pad_w, y+pad_h), (x+w-pad_w, y+h-pad_h), (0, 255, 0), thickness)


def initNumPlateRecognizer(region="eu"):
    alpr = Alpr("eu", "nplate_train/openalpr.conf.in", "nplate_train/runtime_data")
    if not alpr.is_loaded():
        print("Error loading OpenALPR")
        sys.exit(1)
    alpr.set_default_region(region)
    return alpr
    
def getLatLong(region):
    lat,lng = region.location
    print "Latitude : {0}".format(lat)
    print "Longitude : {0}".format(lng)  
    

def getLocation(region):
    #print country
    print "Country : " + region.country
    print "Continent : " + region.continent
    print "TimeZone : " + region.timezone
    getLatLong(region)

if __name__ == '__main__':
    alpr = None    
    #get my public ip-address
    my_ip = urlopen('http://ip.42.pl/raw').read()
    region = geolite2.lookup(my_ip)

    if region is not None:
        getLocation(region)


    #Initializing number-plate recognition
    alpr = initNumPlateRecognizer("eu")
    
        
    img = None
    plt.figure("Recce Demo")
    plt.gray()
    plt.xticks([]),plt.yticks([])
    mpl.rcParams['toolbar'] = 'None'

    for f in range(1424):
        fl = "datasets/I1_{0}.png".format(str(f).zfill(6))
        im=plt.imread(fl)

        #print url
        #values = { 'lat': '0','long': '0' }
        """
        values = { 'lat': '0','long': '0' }
        data = urllib.urlencode(values)
        req = urllib2.Request(url +'?' +  data.encode('utf-8'))
        response = urllib2.urlopen(req)
        result = response.read()
        print result
        """

        #r = requests.post(url, data=values)
        #print(r.status_code, r.reason)


        #detect people
        
        hog = cv2.HOGDescriptor()
        print type(im)
        hog.setSVMDetector( cv2.HOGDescriptor_getDefaultPeopleDetector() )
        print "Hello"
        found, w = hog.detectMultiScale(img, winStride=(8,8), padding=(32,32), scale=1.05)
        print "sds"
        found_filtered = []
        for ri, r in enumerate(found):
            for qi, q in enumerate(found):
                if ri != qi and inside(r, q):
                    break
            else:
                found_filtered.append(r)
        #draw_detections(img, found)
        #draw_detections(img, found_filtered, 3)
        print('%d (%d) found' % (len(found_filtered), len(found)))

        

        #trying to recognize nummber plates from images
        results = alpr.recognize_file(fl)
        #print results
        for plate in results['results']:
            if len(plate['candidates']) > 0:
                print "Found: %12s %12f" % ( plate['candidates'][0]['plate'],plate['candidates'][0]['confidence']) 

        if img is None:
            img = plt.imshow(im)
        else:
            img.set_data(im)
        plt.pause(.05)
        plt.draw()
    alpr.unload()
