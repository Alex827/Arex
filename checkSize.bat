@echo off &setlocal
REM Makes a list of files larger than 100MB to the file largerThan100.txt
REM Then rsyncd can exclude these files.
REM By default only checks 'D:/Data' any additional directories must be manually added


REM for /f "delims=|" %%a IN ('dir /b "D:\Arex\AIS_stuff"') do echo %%~na %%~za
SET /A r=100 * 1000000
copy NUL C:\rsyncd\overSized.tmp

forfiles /p D:\Data /s /c "cmd /c if @fsize gtr %r% echo @relpath"> C:\rsyncd\overSized.tmp

break > C:\rsyncd\overSized.txt
for /f "delims=" %%i in (C:\rsyncd\overSized.tmp) do (
	set "origpath=%%~i"
	setlocal enabledelayedexpansion
	set "origpath=!origpath:~2!"
	set "origpath=!origpath:\=/!"
	echo !origpath!>> C:\rsyncd\overSized.txt
	endlocal
	)

del C:\rsyncd\overSized.tmp
