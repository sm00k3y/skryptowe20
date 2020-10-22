#!/bin/bash

date=$(cat Zakup.txt | ./SelKol.sh 1 | ./StarczyJeden.sh $1 | head -1)
cat Zakup.txt | ./StarczyJeden.sh $date | ./SelKol.sh 4 | ./SumaNum.sh

