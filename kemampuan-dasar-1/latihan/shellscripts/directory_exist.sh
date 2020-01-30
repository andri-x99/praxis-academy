#!/bin/bash
echo "enter directory name"
read ndir
if [ -d "$ndir" ]
then
echo "directory exist"
else
`mkdir $ndir`
echo "directory created"
fi
