#!/usr/bin/python2.7
# -*- coding: utf8 -*-
# ----------------------------------------

## Modules ##
import pygame
import os
import command as Command
import sound as Sound


pygame.init()
Command.Manager
manager = Command.Manager()
Sound.SoundManager
sound = Sound.SoundManager()


print "________________________________________"
print ""
print "   ####    ####  #   #  #######          "
print "   #   #   #     #  #      #             "
print "   # ##    ####  ##        #             "
print "   #   #   #     #  #      #             "
print "   #    #  ####  #   #     #   v1.1      "
print "________________________________________"

manager.CMD_command('command')

while True:

    consol = raw_input('#>: ')
    print ""
    manager.action(consol)
