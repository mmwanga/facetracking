#!/usr/bin/python

import SimpleCV
import time
import simplejson as json
import sys

if __name__ == "__main__":

        matches = 0
        green = (0, 255, 0)
        sleeptime = 2

        try:
                cam = SimpleCV.Camera(0)
        except:
                print "Can't open webcam"
                sys.exit()

        # Run forever
        while 1:
                tstart = time.time()

                try:
                        frame = cam.getImage()
                except:
                        print "Can't grab frame from webcam"
                        sys.exit()

                '''facedetect = frame.findHaarFeatures('haarcascade_frontalface_alt.xml')'''
                facedetect = frame.findHaarFeatures('facetrack-training.xml')

                # Only count if we find a face
                if facedetect:
			facedetect.draw()
			frame.show()
                        # Count all the matches
                        for f in facedetect:
                                matches += 1
                faces = {"faces": matches, "taken": time.time()}

                tfinish = time.time()
                faces['elapsed'] = tfinish - tstart

                facesjson = json.dumps(faces)
		print(facesjson)
                matches = 0
                time.sleep(sleeptime)

        sys.exit()
