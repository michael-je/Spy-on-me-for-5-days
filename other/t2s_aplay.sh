#!/bin/bash
pico2wave -w=/tmp/t2s.wav "$1"
aplay /tmp/t2s.wav
rm /tmp/t2s.wav