#!/bin/bash

find . -type f -iname "*.java" >> x
file="x"

while IFS= read line
do
echo "ada file java di direktory $line"

done <"$file"

rm x

#https://www.cyberciti.biz/faq/bash-foreach-loop-examples-for-linux-unix/
#https://www.cyberciti.biz/faq/unix-howto-read-line-by-line-from-file/
