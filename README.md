Raspberry Pi Security Camera
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

## Email yourself when something moves!
In motion, you can configure a command to run whenever motion is detected with the `on_motion_detected` option in motion.config. I set this to trigger email_on_motion.py whenever something moves.

email_on_motion.py will send an email to the addresses you configure that includes an attachment of the most recent still snapshot captured by the camera. If you configure motion to store images while motion is detected, you can be alerted with a still image of the subject immediately when it happens!

To configure email_on_motion.py, just set the following constants in the file:

`MOTION_OUTPUT_DIRECTORY`: The directory where motion is outputting images.
`SMTP_SERVER`: The email server that will be sending the outgoing emails. (String)
`FROM_ADDRESS`: The email address you will send the messages from. (String)
`TO_ADDRESSES`: A list of email addresses to send the email message to (List of Strings)
`USERNAME`: The username for the email server that will send the emails (String)
`PASSWORD`: The password for the email server (String)

In motion.conf (I have published mine as an example), just configure on_motion_detected to trigger the script. Adding "gap 10" after will delay 10 seconds before sending the email (ensuring the image has been captured and saved):

    on_motion_detected /home/pi/raspberrypi_security_cam/email_on_motion.py gap 10

Just make sure to set the script to be executable:

    chmod +x /home/pi/raspberrypi_security_cam/email_on_motion.py

