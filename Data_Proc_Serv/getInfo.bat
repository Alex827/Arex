break > D:\%computername%servInfo.log
wmic logicaldisk get deviceid,volumename /format:csv | more | findstr /v DeviceID >> D:\%computername%servInfo.log

tasklist /FI "IMAGENAME eq MATLAB.exe" 2>NUL | find /I /N "MATLAB.exe">NUL
if "%ERRORLEVEL%"=="0" echo Matlab,running >> D:\%computername%servInfo.log
if "%ERRORLEVEL%"=="1" echo Matlab,notrunning >> D:\%computername%servInfo.log