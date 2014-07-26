raspberrypi_security_cam
========================

A collection of scripts for running an intelligent security camera using a Raspberry Pi with an attached camera.

Uses the [Motion](http://www.lavrsen.dk/foswiki/bin/view/Motion/WebHome) open source application to monitor the video feed from the camera and detect motion.

The camera will be running as long as the system is up. I have configured motion following [this guide](http://www.codeproject.com/Articles/665518/Raspberry-Pi-as-low-cost-HD-surveillance-camera) to store several still shots and a very short avi movie when motion is detected.

# How To Use

## Image Cleanup Script
In my Raspberry Pi, I am only using an 8GB SD card, so I don't want to store very many images. I will be emailing/uploading them to a remote server when motion is detected, so I plan to clear the store of images and videos once per day.

To do this, edit cleanup_images_dir.sh to configure the following:

`OUTPUT_LOCATION`: The absolute path of the directory where motion outputs the image files to clean up.
`STALE_LIMIT`: The amount of time, in minutes, for which any files with a modified date that is older will be deleted.

I am running this as a chron task once per day, to make sure I don't fill up my SD card with images.
