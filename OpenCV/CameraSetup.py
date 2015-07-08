# RASPBERRY PI CAMERA SETUP
# sudo raspi-config
# enable camera
# sudo apt-get update
# sudo apt-get install python-picamera
# sudo apt-get install python3-picamera
# -----------------------------------------

import picamera
# from time import sleep

camera = picamera.PiCamera()

# camera.hflip = True
# camera.vflip = True
# camera.sharpness = 0
# camera.contrast = 0
# camera.brightness = 50
# camera.saturation = 0
# camera.ISO = 0
# camera.video_stabilization = False
# camera.exposure_compensation = 0
# camera.exposure_mode = 'auto'
# camera.meter_mode = 'average'
# camera.awb_mode = 'auto'
# camera.image_effect = 'none'
# camera.color_effects = None
# camera.rotation = 0
# camera.hflip = False
# camera.vflip = False
# camera.crop = (0.0, 0.0, 1.0, 1.0)

# camera.start_preview()
# camera.stop_preview()

camera.capture('image.jpg')
# sleep(10)
