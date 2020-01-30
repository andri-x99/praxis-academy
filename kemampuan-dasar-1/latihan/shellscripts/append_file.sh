#!/bin/bash
echo "before appending the file"
cat book.txt

echo "learning bash script" >> book.txt
echo "after appending the file"
cat book.txt
