@ECHO OFF

Zad1-KodPowrotu\KodPowrotu /s %*

IF %ERRORLEVEL% LSS 10 (
	ECHO Przekazano: prawdilowa wartosc
)

IF %ERRORLEVEL% EQU 11 (
	ECHO Brak parametrow
)

IF %ERRORLEVEL% EQU 12 (
	ECHO Parametr %1 nie jest cyfra
)

IF %ERRORLEVEL% EQU 13 (
	ECHO Niewlasciw ailosc parametrow
)
