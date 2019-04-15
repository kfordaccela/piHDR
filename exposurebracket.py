import picamera
import time
from time import sleep
from fractions import Fraction

# This script captures exposures with varying shutter time. 
# The frame rate needs to be longer than the exposure or it won't work. 
# The capture takes as long as the frame rate, so reducing the frame rate saves time for quick exposures.
#
# Exposure time below (shutter_speed) is in micro seconds 1000000 is 1 second, will write some functions
# to set the fram rate correctly for the camera prior to using these exposures.

class hdrCamera:
    # camera = picamera.PiCamera()
    def __init__(self,name,baseIso):
        self.baseIso = 200;
        # list of acceptable ISO's
        self.isos = [60,100,200,400,800]
        self.name = name
        self.camera = picamera.PiCamera()
        self.baseExposure = 0
        self.baseIso = baseIso
        if not baseIso in self.isos:
            print("Iso ",baseIso," is not a valid starting iso please use 60,100,200,400,800")
        # This allows for use to detect the camera for optomal resolution
        # if we don't get the module correct then we may loose some
        # resolution from the camera thout could be used
    def detectCamera(self):
        print("Camera Version: ",self.camera.revision)
        # if the camera is version 2 attempt to use the better resolution
        if (camera.revision).upper() == "IMX219":
            try:
            camera.resolution = (3280,2464)
            except:
            print("Review readme for change in memory split to full support Camera v2")
            print("Resolution kept at 2592x1944")
                camera.resolution = (2592,1944)
        else: 
        #(camera.revision).upper() <> "IMX219":
            camera.resolution = (2592,1944)
	    # print("detecting camera")
    ## Just a test
    def takePhoto(self):
        print("Hello World")
    ## Define a camera
    def initCamera(self):
        #camera = picamera.PiCamera()
        #camera.awb_mode = 'off'
        self.camera.awb_mode = 'off'
        self.camera.awb_gains = (1.8,1.8)
        self.camera.framerate = 15
        self.camera.iso = 200
        print("hello there")
    def checkExposure(self):
        self.camera.start_preview()
        sleep(2)
        self.baseExposure = self.camera.exposure_speed()
        print("base exposure found: ",baseExposure)
    def convertMicroSeconds(self):
        self.baseExposure = self.baseExposure * 1000000
        self.fpsCalc = 1/self.baseExposure
        # Adjust the iso if possable
        if self.fpsCalc > 60:
            self.camera.iso = baseIso/4
        if self.fpsCalc > 30:
            self.camera.iso = baseIso/2
        if self.fpsCalc < 7.5:
            self.camera.iso = baseIso*2 
        if self.fpsCalc < 3.75:
            self.camera.iso = baseIso*4
        # Set framerate
        if self.fpsCalc >= 15:
            self.camera.framerate = 15
        if self.fpsCalc < 15:
            self.camera.framerate = self.fpsCalc
        checkExposure()	
def main():
  takeImages = hdrCamera("hello there",200)
  takeImages.takePhoto()
  takeImages.initCamera()
  # print("Camera Version: ",camera.revision)
  print("Camera Version: ",takeImages.detectCamera())
  ## Camera Version 1
  # camera.resolution = (2592,1944)
  ## Camera Version 2
  # camera.resolution = (3280,2464)
'''
  #with picamera.PiCamera() as camera:
  camera = picamera.PiCamera()
  ## Basic Settings
  # camera.exposure_mode = 'off'

  start = time.time()

  ## Set framerate and iso
  isoSet = time.time()
  # camera.start_preview()
  print("time to set iso: ",time.time() - isoSet)
	
  ## Set Resolution
  print("time to set resolution: ",time.time() - start)

  ## Wait for things to stabelize and then output shutter speed
  camera.start_preview()
  sleep(2)
  baseExposure = camera.exposure_speed
  print(baseExposure)

  ## Take a test image
  # camera.capture('testImage.jpg')
  startCatputer = time.time()
  #0.8s exposure
  # camera.framerate = 1
  # camera.shutter_speed = baseExposure*6
  # camera.capture('ldr_01.jpg')
  camera.shutter_speed = baseExposure*4
  camera.capture('ldr_02.jpg')
  #0.2s exposure
  # camera.framerate = 5
  # camera.shutter_speed = baseExposure*2
  # camera.capture('ldr_02.jpg')
  #0.05s exposure
  # camera.framerate = 20
  camera.shutter_speed = baseExposure*1
  camera.capture('ldr_03.jpg')
  #0.0125s exposure
  # camera.framerate = 30
  # camera.shutter_speed = int(baseExposure/2)
  # camera.capture('ldr_04.jpg')
  #0.003125s exposure 
  camera.shutter_speed = int(baseExposure/4)
  camera.capture('ldr_05.jpg')
  #0.0008s exposure
  camera.shutter_speed = int(baseExposure/8)
  camera.capture('ldr_06.jpg')
  finish = time.time()
  print("Captured images in: ",(finish-startCatputer))
'''
if __name__ == "__main__":
	main()
