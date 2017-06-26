#!/bin/sh
USER='SWAL'
PASSWD='SBARCa1$data'

ftp -A -i -n aisdata.sbarc.org << SCRIPT1 
quote USER $USER
quote PASS $PASSWD
lcd /home/aisadmin/AISdata_logfiles/SBARC
ls . filesList.txt
exit 
SCRIPT1

ls /home/aisadmin/AISdata_logfiles/SBARC/ > clientFiles.txt

python splitLSfiles.py 

exit 0
