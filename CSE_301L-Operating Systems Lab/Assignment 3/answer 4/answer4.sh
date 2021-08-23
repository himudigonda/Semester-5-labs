SRC="./alpha/"
DST="./beta/"

for f in $DST/*; do
    #echo Processing $f
    if [ -f $f ]; then
        tFile="$SRC/$(basename $f)"
        aFile="$DST/$(basename $f)"
        if [ -f $tFile ]; then
            sFile=$(cat $SRC/$(basename $f))
            dFile=$(cat $DST/$(basename $f))
            if [ "$sFile" = "$dFile" ]; then
                echo "$sFile $dFile yes"
                echo -n "Deleting $aFile..."
                /bin/rm $aFile
                [ $? -eq 0 ] && echo "done" || echo "failed"
            else
                echo "$sFile $dFile no"
                echo "File contents are different, so skipping"
            fi

        fi
    fi
done
