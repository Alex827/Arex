Author: Alex Luu
Email: luualex827@gmail.com
Date: 07/28/2017
Version: 1.0
Description: AutoMounting Script that will mount new harddrives to the directory 'E:\MountPoints\[harddrive's name]'
		It also changes permissions on the volumes itself. It will add in read and execute permissions to the
		'Students' group and remove the group 'Authenticated Users' which gives everyone full control ( not wanted ).
Files:
	* automount.ps1 = the main script that does everything
	* cleanup.ps1 = the script that helps clean up the directories of the drives that are not plugged in
	* diff.txt = the new harddrives in GUID form
	* diffVol.csv = the csv file for the new harddrives volume label and GUID
	* mountVolCmp.txt = the newest list of all the volumes plugged in
	* mountVolOri.txt = the original list of all the volumes (DO NOT DELETE/MODIFY) there will be a backup
	* mountVolOriBak.txt = back up of the original file
	* README.txt = this file
	* toRunAutoMount.ps1 = the script to put in task scheduler that will only run when new harddrives are plugged in
	* schedulerLog.log = the log file from the task scheduler background service to help with debugging
	* System.adm = back up file of System.adm
	* WindowsExplorer = back upf file of WindowsExplorer.admx

Notes:
	* I have changed the WindowsExplorer.admx file to edit the Group Policy Object.
		The change is in User Configuration > Policies > Administrative Templates > Windows Components > File Explorer
		In 'Hide these specified drives in My Computer', I have editted the setting for 'Restrict all drives' to actually be
		restrict all drives except the E drive ( which is the UserData drive ). This is to allow the 'Students' group to
		access only the E drive.

	* I have set-up a 'Students' group when creating new user accounts. The 'Students' group has the Group Policy Object called 
		'Non-Admin', which has all default settings except for the above mentioned 'Restrict all drives' setting changed.
		Please change all necessary settings for security and correct usage purposes.

	* I had to change volume permissions because of the way Windows mount points work. You can set up permissions for the mount point
		directory, but those permissions do not apply to the volume itself. You must change the volume permissions in order for
		the permissions to have any effect.

	* For more confusion, please contact me with luualex827@gmail.com or contact Bruce Thayre.