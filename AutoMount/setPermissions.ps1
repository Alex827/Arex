# if csv exists then import and do the loop
if ([System.IO.File]::Exists('C:\AutoMount\diffVol.csv')) {
	# import the csv
	$file = import-csv .\diffVol.csv

	# for loop to loop through csv
	$file | foreach-object {
		# gets the GUID of the volume
		$devID = $_.deviceid

        # set icacls options
        $grant = "PKFast\Students:(OI)(CI)(RX)"
        $remove = "Authenticated Users"

		# stops of they are default volume GUIDs
		# C drive
		if ($devID -eq "\\?\Volume{692ec8c6-0000-0000-0000-501f00000000}\") {return}
		# CD drive?
		elseif ($devID -eq "\\?\Volume{cb6dc4f5-7191-11e7-ab96-806e6f6e6963}\")  {return}
		# D/Data drive
		elseif ($devID -eq "\\?\Volume{5b5df6cc-739b-4e41-a901-009886b3e002}\")  {return}
		# E/User Data drive
		elseif ($devID -eq "\\?\Volume{07b3df25-3ae6-4b69-a4af-91ceafc89203}\")  {return}

        # checks if the volume already has permissions, only set permissions if not it was not already set
        $permStr = icacls $devID
        #echo $permStr
        if(-not ($permstr -match "Students")) {
            #write-host "there is no students for" $devID 
            
            # run icacls options to set permissions for the volume itself
            "New harddrive detected. Changing permissions."
            icacls $devID /grant ""$grant""
            icacls $devID /remove ""$remove""
            "Permissions changed."
            
        }
        #else{ echo "there is students for" $devID }
	}
}