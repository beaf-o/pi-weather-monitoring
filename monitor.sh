#!/bin/bash

dir="/home/pi/monitor"
dateSuffix=`date +'%Y-%m-%d'`

cd $dir

rm -rf webcam/*
rm -rf strikes/*
rm -rf rain/*

python $dir/get_data.py 2>&1 | tee -a $dir/logs/get_data_${dateSuffix}.log &
python $dir/show_data.py 2>&1 | tee -a $dir/logs/show_data_${dateSuffix}.log &
