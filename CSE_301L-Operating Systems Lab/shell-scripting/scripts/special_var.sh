#! /bin/bash

# $0
# $1-$9
# $#
# $*
# $@
# $?
# $$

echo $0
echo $1' and '$2
echo $#
echo $*
rm -rf non_existing_file.sh
echo $?
echo $$
