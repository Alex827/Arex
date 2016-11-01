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
ls . filesList.txt
exit 
SCRIPT1

#gets LS of files on client side
printf "Getting client file names\n"

ls /home/aisadmin/AISdata_logfiles/SBARC/ > clientFiles.txt

#python script to format the LS files from server
printf "Splitting server file names\n"
python splitLSfiles.py

#python script to find missing files in client side
printf "Differencing server and client file names\n"

#saves all the missing filenames as an array
ARROFNAMES=($(python diffLSfiles.py))

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
	get $i
	exit 
SCRIPT2
	done
#print this message if there are no files
else
	printf "There are no missing files\n"
fi
#print done when done
printf "Done\n"

exit 0
