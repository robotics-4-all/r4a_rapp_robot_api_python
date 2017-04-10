#!/usr/bin/env python

import time
import sys

################################# PORTABLE ####################################
sys.path.append('../pynaoqi-python2.7-2.1.4.13-linux64')
sys.path.append('python/abstract_classes')
sys.path.append('python/implementations/nao_v4_naoqi2.1.4')

from rapp_robot_api import RappRobot
rh = RappRobot(ip = "192.168.0.245", port = "9559")

rh.audio.setVolume(50)
rh.audio.speak("Hello")
