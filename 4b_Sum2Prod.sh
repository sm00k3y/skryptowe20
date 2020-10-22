#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Specify two product names as arguments"
else
    names=$(cat Zakup.txt | ./SelKol.sh 2 | ./StarczyJeden.sh $1 $2)
    cat Zakup.txt | ./StarczyJeden.sh $names | ./SelKol.sh 3 | ./SumaNum.sh
fi

