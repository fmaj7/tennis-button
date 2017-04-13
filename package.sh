#!/usr/bin/env sh

rm -f tennis_tracker.zip && zip -r tennis_tracker.zip ./*
ZIP_FILE_PATH=$(realpath tennis_tracker.zip)
cd $VIRTUAL_ENV/lib/python2.7/site-packages/
zip -r $ZIP_FILE_PATH ./*
