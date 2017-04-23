#!/usr/bin/env zsh

aws lambda update-function-code --function-name iotbutton_G030MD02009201V8_iot-button-sms-python --zip-file fileb://tennis_button.zip --publish
