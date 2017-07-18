break > D:\Arex\info.log
wmic logicaldisk get deviceid,volumename /format:csv | more | findstr /v DeviceID >> D:\Arex\info.log

tasklist /FI "IMAGENAME eq MATLAB.exe" 2>NUL | find /I /N "MATLAB.exe">NUL
if "%ERRORLEVEL%"=="0" echo Matlab is running >> D:\Arex\info.log
if "%ERRORLEVEL%"=="1" echo Matlab is not running >> D:\Arex\info.log