#!/bin/bash
echo "wait command" &
process_id=$!
wait $process_id
echo "exited with status $?"
