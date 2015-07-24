#!/bin/bash

dir="/home/pi/monitor"

cd $dir
python $dir/get_data.py 2>&1 | tee -a $dir/logs/get_data.log &
python $dir/show_data.py 2>&1 | tee -a $dir/logs/show_data.log &
