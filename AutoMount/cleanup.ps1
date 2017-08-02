# Cleans up the E:\MountPoints by deleting the directories for harddrives that are not plugged in/don't exist anymore
# if csv exists then import and do the loop
if ([System.IO.File]::Exists('C:\AutoMount\diffVol.csv')) {
	# import the csv
	$file = import-csv .\diffVol.csv
    # get all the folders in E:\MountPoints\
    $folders =  Get-ChildItem ('E:\MountPoints\') -Name
    # var to see if we need to delete or not; 0 = don't delete; 1 = do delete
    $toDel = 1

    # go through all the folders in E:\MountPoints\
    $folders | ForEach-Object {
        # gets the folder name
        $folderName = $_
        $toDel = 1
        # go through all currently mounted drives
        $file | foreach-object {
            # gets the label of the volume
		    $name = $_.label
		    # stops if they are default volume labels
		    if ($name -eq "Data") {return}
		    elseif ($name -eq "UserData")  {return}
		    elseif ($name -eq "System Reserved")  {return}

            # if there is a match then do not delete
            if ($folderName -eq $name) {
                $toDel = 0
                return
            }
            <## if there is no match then delete
            if ($folders -ne $name) {
            } #>
        }
        # check to delete or not
        if ($toDel -eq 1) {
            Remove-Item -path E:\MountPoints\$folderName -Force
        }
    }
}