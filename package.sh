#!/usr/bin/env sh
FILE_NAME=tennis_button.zip
rm -f $FILE_NAME && zip -r $FILE_NAME ./*
ZIP_FILE_PATH=$(realpath $FILE_NAME)
cd $VIRTUAL_ENV/lib/python2.7/site-packages/
zip -r $ZIP_FILE_PATH ./*
