#!/bin/bash
eval "$(conda shell.bash hook)"

videos=("clip1" "clip2" "clip3" "clip4" "clip5")
track_thresh=0.8
track_buffer=30
match_thresh=0.8

# activate env
conda activate MixSort2

for vid in "${videos[@]}"; do
    python3 tools/demo_track_per_player.py \
        -expn yolox_x_sports_mix \
        -f exps/example/mot/yolox_x_sportsmot.py \
        --track_thresh $track_thresh \
        --track_buffer $track_buffer \
        --match_thresh $match_thresh \
        -c pretrained/yolox_x_sports_mix.pth.tar \
        -n yolox_x_sports_mix \
        --path "./videos/$vid.mp4" \
        --save_result \
        video
done