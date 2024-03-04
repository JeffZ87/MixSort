#!/bin/bash

videos=("clip1" "clip2" "clip3" "clip4" "clip5")
conda activate MixSort2
for vid in "${videos[@]}"; do
    python3 tools/demo_track_per_player.py \
    -expn yolox_x_sports_mix \
    -f exps/example/mot/yolox_x_sportsmot.py \
    -c pretrained/yolox_x_sports_mix.pth.tar \
    -n yolox_x_sports_mix \
    --path "./videos/$vid.mp4" \
    --save_result \
    video

done