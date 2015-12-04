#!/usr/bin/python3

import flotilla
import time
import pygame
import glob
import re
import random

def natural_sort_key(s, _nsre=re.compile('([0-9]+)')):
    return [int(text) if text.isdigit() else text.lower() for text in re.split(_nsre, s)]

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()
pygame.mixer.set_num_channels(32)

patches = glob.glob('drums/*')
samples = [pygame.mixer.Sound(patch) for patch in patches]

notes = glob.glob('piano/*.wav')
notes.sort(key=natural_sort_key)
piano = [pygame.mixer.Sound(note) for note in notes]

speed = 1

arp_pattern = []
pattern = []
play_note = 0
seq_length = 8

def regen_arp_pattern():
    global arp_pattern
    arp_pattern = [random.randint(0,12) for x in range(seq_length)]

def regen_pattern():
    global pattern
    pattern = [random.choice(samples) for x in range(seq_length)]

regen_pattern()
regen_arp_pattern()

@flotilla.on("update")
def synth_update():
    pass

@flotilla.on("dial")
def synth_dial(data):
    global play_note
    print(data)
    note = (int(data[0]) / 1023.0)
    note = int(note * len(piano))
    play_note = note

@flotilla.on("slider")
def synth_slider(data):
    global speed
    value = int(data[0])
    print("Slider value: {}".format(value))
    speed = 0.1 + ((value/1023.0)*0.9)


@flotilla.on("light")
def synth_light(data):
    value = int(data[0])
    print("Light value: {}".format(value))

@flotilla.on("touch")
def synth_touch(data):
    one, two, three, four = [int(d) for d in data]
    print(one, two, three, four)
    if one:
        regen_pattern()
    if two:
        regen_arp_pattern()
    if three:
        samples[3].play(loops=0)
    if four:
        samples[4].play(loops=0)

#flotilla.on('slider',synth_slider)
#flotilla.on('touch',synth_touch)

@flotilla.on("ready")
def synth_main():
    global pattern

    on = 50
    beat = [on,0,0] + ([0,0,0] * 3)
    metro = [0,0,on]
    x = 0
    
    while True:
        flotilla.modules[6].set_rainbow(metro + beat)
        pattern[x].play(loops=0)

        arp = play_note
        arp += arp_pattern[x]
        arp %= len(piano)
        piano[arp].play(loops=0)
        
        x+=1
        x%=seq_length
        time.sleep(speed)
        beat = beat[3:] + beat[:3]
        if metro == [0,0,on]:
            metro = [0,on,0]
        else:
            metro = [0,0,on]

flotilla.run()
flotilla.wait()
