#! /bin/bash
#! @author: @ruhend (Mudigonda Himansh)
#! Assignment 4

c="r"
chr="rim"
str="raj raced around the rough ring really rashly"


echo "************************************************************"
echo $str
echo "************************************************************"
echo $str | perl -ne "print s/$c/$chr/g"
echo ""
echo "************************************************************"
echo $str | sed "s/$c/$chr/g"
echo "************************************************************"