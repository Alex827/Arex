#!/bin/sh

#File: ftpscript.sh
#Author: Arex
#Function: Pulls AIS data files from server into cetus 

USER='SWAL'
PASSWD='SBARCa1$data'
ARROFNAMES=()

#connects to ftp to get LS of files on server
printf "Connecting to FTP\n"

ftp -A -i -n aisdata.sbarc.org > /dev/null << SCRIPT1 
quote USER $USER
quote PASS $PASSWD
lcd /home/aisadmin/AISdata_logfiles/SBARC
ls . serverls.txt
exit 
SCRIPT1

mv ~/AISdata_logfiles/SBARC/serverls.txt /tmp/

#gets LS of files on client side
printf "Getting client file names\n"

ls -l /home/aisadmin/AISdata_logfiles/SBARC/ > /tmp/clientls.txt

#saves all the missing filenames as an array
ARROFNAMES=($(python checkNewFiles.py))

#loop through each file and download them through ftp
#if there are files to download
if [ ${#ARROFNAMES[@]} -gt 0 ]; then
	printf "Downloading missing files\n"
	for i in "${ARROFNAMES[@]}"
		do
		printf "Now downloading $i\n"	
ftp -A -i -n aisdata.sbarc.org > /dev/null << SCRIPT2 
	quote USER $USER
	quote PASS $PASSWD
	lcd /home/aisadmin/AISdata_logfiles/SBARC
	binary
	get $i
	exit 
SCRIPT2
	done
#print this message if there are no files
else
	printf "There are no missing files\n"
fi

#update the client ls files because we might have downloaded new files
ls -l /home/aisadmin/AISdata_logfiles/SBARC/ > /tmp/clientls.txt

#check for problem files
python checkProblemFiles.py

#print done when done
printf "Done\n"

exit 0
