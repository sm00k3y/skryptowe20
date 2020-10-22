#!/bin/bash

awk_column_args=''
for arg in $@; do
    awk_column_args+="\$$arg,"
done

awk_column_args=${awk_column_args%?}

awk -v OFS="\t" "{print $awk_column_args}"

