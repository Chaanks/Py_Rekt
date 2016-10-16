#!/usr/bin/python2.7
# -*- coding: utf8 -*-
# ----------------------------------------

## Modules ##
import os
import pygame
import subprocess

class SoundManager :
    """Liste des sons"""
    path = "Sound/"

    def __init__(self):
        self.soundList = os.listdir( SoundManager.path )

    def getList( self ):
        return self.soundList

    def selectSound (self, soundId):
        if soundId >= len(self.soundList):
            return False

        path = self.path + self.soundList[soundId]
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
        return True

    def stopSound (self):
        pygame.mixer.music.stop()
