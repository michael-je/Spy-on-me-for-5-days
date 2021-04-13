#!/bin/bash

sed -i "s|mpv_mutex 1|mpv_mutex 0|" $(dirname $(realpath $0))/states.txt