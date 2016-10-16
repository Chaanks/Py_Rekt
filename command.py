#!/usr/bin/python2.7
# -*- coding: utf8 -*-
# ----------------------------------------

## Modules ##
import subprocess
import pygame
from sound import *
import time
import random
import collections

class Manager :
    "Gère les commandes"

    def __init__( self ):
        self.command = {
            'eject':self.CMD_eject,
            'exit' :self.CMD_exit,
            'play':self.CMD_play,
            'sound':self.CMD_sound,
            'command':self.CMD_command,
            'stop':self.CMD_stop,
            'volume+':self.CMD_volumeM,
            'volume-':self.CMD_volumeP,
            'mamadou':self.CMD_mamadou
        }

        self.command = collections.OrderedDict(sorted(self.command.items(), key=lambda t: t[0]))


    def action(self, command):
        if len(command):
            command = command.split()

            if (command[0] in self.command):
                self.command[ command[0] ]( command[1:] )

    def CMD_sound(self, command):
        print ""
        print "------------------"
        print "- Liste des sons -"
        print "------------------"
        s = SoundManager()
        for i in xrange (0,len(s.getList())):
            print i,":",s.getList()[i]
        print ""


    def CMD_eject(self, command):
        subprocess.Popen('eject')

    def CMD_exit(self, command):
        exit(0)

    def CMD_play(self, command):
        s = SoundManager()
        s.selectSound( int( command[0] ) )

    def CMD_command(self, command):
        print ""
        print "-----------------------"
        print "- Liste des commandes -"
        print "-----------------------"
        for i in self.command:
            print "-",i
        print ""

    def CMD_stop (self, command):
        s = SoundManager()
        s.stopSound()

    def CMD_volumeP (self, command):
        subprocess.call(["amixer", "-D", "pulse", "sset", "Master", "100%"])

    def CMD_volumeM (self, command):
        subprocess.call(["amixer", "-D", "pulse", "sset", "Master", "0%"])

    def CMD_mamadou (self, command):
        pygame.mixer.music.load("Sound/SadTroll.mp3")
        pygame.mixer.music.play()

        fen=pygame.display.set_mode((650,342),pygame.FULLSCREEN, pygame.NOFRAME)
        img=pygame.image.load('Picture/mamadou.png').convert()
        pygame.display.flip()

        i = 0
        while i <= 200:
            x= random.randint(0,610)
            y= random.randint(0,302)
            i += 1
            fen.blit(img,(x,y))
            pygame.display.flip()
            time.sleep(0.1)

        pygame.mixer.music.load("Sound/screamer.mp3")
        pygame.mixer.music.play()
        time.sleep(0.25)

        img2=pygame.image.load('Picture/screamer.jpg').convert()
        fen.blit(img2,(0,0))
        pygame.display.flip()
        time.sleep(2)
        pygame.mixer.music.stop()
        pygame.display.quit()
