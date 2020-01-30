#!/bin/bash
filename=$1
if [ -f "$filename" ]; then
echo "file exist"
else
echo "file does not exist"
fi
