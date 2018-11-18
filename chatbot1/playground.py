#!/usr/bin/python2
### 20181117
### Yuqiong Li

import aiml
import sys
import os

os.chdir('/media/yuqiong/DATA/rosproj/chatbot/aiml_data_files')
bot = aiml.Kernel()  # load the aiml file
bot.setBotPredicate("name", "ROBIN")

if os.path.isfile("standard.brn"):
    # if the brain file already exists
    bot.bootstrap(brainFile="standard.brn")
else:
    # create the brain file from learn files and save brain
    bot.bootstrap(learnFiles="../startup.xml", commands="LOAD AIML B")
    bot.saveBrain("standard.brn")

while(True):
    print bot.respond(raw_input("Enter input >"))
