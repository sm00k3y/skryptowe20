#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Specify one product name as argument"
else
    name=$(cat Zakup.txt | ./SelKol.sh 2 | ./StarczyJeden.sh $1)
    cat Zakup.txt | ./StarczyJeden.sh $name | ./SelKol.sh 3 | ./SumaNum.sh
fi

