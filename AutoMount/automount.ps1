# get list of volumes
mountvol | findstr ? > mountvolCmp.log
# diff the new list with original list of hard drives to find out which ones are new hard drives
diff (get-content .\mountvolCmp.log) (get-content .\mountvolOri.log) | format-wide -property inputobject -column 1 > diff.log

# formats the list of diff
(gc .\diff.log)|?{$_.trim() -ne ""}|set-content .\diff.log

# export the diff'ed volumes to a csv
foreach($line in get-content .\diff.log) {
	get-wmiobject win32_volume | select-object label,deviceid | export-csv -path .\diffVol.csv
}

# if no diff then clear csv file
if ([System.IO.File]::Exists('C:\AutoMount\diffVol.csv')) {
	if ((get-content .\diff.log) -eq $Null) {
		clear-content .\diffVol.csv
	}
}

# if csv exists then import and do the loop
if ([System.IO.File]::Exists('C:\AutoMount\diffVol.csv')) {
	# import the csv
	$file = import-csv .\diffVol.csv

    C:\AutoMount\setPermissions.ps1

	# for loop to loop through csv
	$file | foreach-object {
		# gets the label of the volume
		$name = $_.label
		# gets the GUID of the volume
		$devID = $_.deviceid
        
		# stops if they are default volume labels
		if ($name -eq "Data") {return}
		elseif ($name -eq "UserData")  {return}
		elseif ($name -eq "System Reserved")  {return}

		# make directories for these volume
		New-Item -ItemType Directory -Force -Path E:\MountPoints\$name | Out-Null

		# stops of they are default volume GUIDs
		# C drive
		if ($devID -eq "\\?\Volume{692ec8c6-0000-0000-0000-501f00000000}\") {return}
		# CD drive?
		elseif ($devID -eq "\\?\Volume{cb6dc4f5-7191-11e7-ab96-806e6f6e6963}\")  {return}
		# D/Data drive
		elseif ($devID -eq "\\?\Volume{5b5df6cc-739b-4e41-a901-009886b3e002}\")  {return}
		# E/User Data drive
		elseif ($devID -eq "\\?\Volume{07b3df25-3ae6-4b69-a4af-91ceafc89203}\")  {return}
	
		# add mount point to shared directory 'E:\MountPoints\[name of volume]'
		Get-WmiObject -class Win32_Volume | where-object {$_.DeviceID -Like "$devID"} | foreach-object -process {$_.AddMountPoint("E:\MountPoints\$name")} | Out-Null

	}
}

# run clean up script
C:\AutoMount\cleanup.ps1