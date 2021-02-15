# Python-gmail-bot
## Python app to fast organize gmail with labels

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This app is using Google API. It allows to create new label, and add messages from specific sender.\
For example:\
You have 10 mails in your inbox. And 6 of all messages are from Google.\
You want to have all this mails in one place (here we can use labels)\
This app will create new label, and add label tag into all messages from Google.

## Technologies
Project is created with:
* Python 3.8
* Gmail API

## Setup (IMPORTANT!)
DEMO ON YOUTUBE: https://youtu.be/zuCEpqoPXr4

Probably you may have to allowed to use "less secure app" in setting on your Gmail account !!!

Step 1:\
Turn on your Gmail API (link below) and download file 'credenials.json'. Next add this file into directory with this app.
https://developers.google.com/gmail/api/quickstart/python#step_1_turn_on_the

Step 2:\
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

Step 3:\
run gmail_bot.py

Step 4:\
Chose your gmail account, next accept all permissions

Step 5:\
Follow program commands
