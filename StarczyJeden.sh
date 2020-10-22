#!/bin/bash

while read line; do
    for arg in $@; do
        if echo $line | grep -q "$arg"; then
            echo $line
        fi
    done
done

