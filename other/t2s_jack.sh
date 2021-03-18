#!/bin/bash
pico2wave -w=/tmp/t2s.wav "$1"
cvlc --play-and-exit --audio-desync 50 /tmp/t2s.wav
rm /tmp/t2s.wav