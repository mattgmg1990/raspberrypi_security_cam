#! /bin/sh

OUTPUT_LOCATION='/home/pi/motion'
FILE_PATTERN_TO_DELETE_JPG='*.jpg'
FILE_PATTERN_TO_DELETE_AVI='*.avi'
# Time in minutes (24 hours)
STALE_LIMIT='1440'

# Delete all files at $OUTPUT_LOCATION that match $FILE_PATTERN_TO_DELETE and are older than $STALE_LIMIT
$(find $OUTPUT_LOCATION -name $FILE_PATTERN_TO_DELETE_AVI -type f -mmin +$STALE_LIMIT -delete)
$(find $OUTPUT_LOCATION -name $FILE_PATTERN_TO_DELETE_JPG -type f -mmin $STALE_LIMIT -delete)
