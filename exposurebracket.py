import picamera
import time
from time import sleep
from fractions import Fraction

# This script captures exposures with varying shutter time. 
# The frame rate needs to be longer than the exposure or it won't work. 
# The capture takes as long as the frame rate, so reducing the frame rate saves time for quick exposures.

class Camera:
	## Just a test
	def takePhoto(frameRate,sSpeed,captureFile):
		print("Hello World");
	## Define a camera

with picamera.PiCamera() as camera:
    ## Basic Settings
    # camera.exposure_mode = 'off'
    camera.awb_mode = 'off'
    camera.awb_gains = (1.8,1.8)

    start = time.time()
    ## Set Resolution
    camera.resolution = (2592,1944)
    print("time to set resolution: ",time.time() - start);

    ## Set framerate and iso
    isoSet = time.time()
    camera.framerate = 30 
    camera.iso = 200
    # camera.start_preview()
    print("time to set iso: ",time.time() - isoSet);

    ## Wait for things to stabelize and then output shutter speed
    sleep(2)
    baseExposure = camera.exposure_speed
    print(baseExposure)

    ## Take a test image
    # camera.capture('testImage.jpg')
    startCatputer = time.time()
    #0.8s exposure
    # camera.framerate = 1
    camera.shutter_speed = baseExposure*4
    camera.capture('ldr_01.jpg')
    #0.2s exposure
    # camera.framerate = 5
    camera.shutter_speed = baseExposure*2
    camera.capture('ldr_02.jpg')
    #0.05s exposure
    # camera.framerate = 20
    camera.shutter_speed = baseExposure*1
    camera.capture('ldr_03.jpg')
    #0.0125s exposure
    # camera.framerate = 30
    camera.shutter_speed = baseExposure/2
    camera.capture('ldr_04.jpg')
    #0.003125s exposure 
    camera.shutter_speed = baseExposure/4
    camera.capture('ldr_05.jpg')
    #0.0008s exposure
    #camera.shutter_speed = baseExposure/6
    #camera.capture('ldr_06.jpg')
    finish = time.time()
print("Captured images in: ",(finish-startCatputer))

