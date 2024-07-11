@echo off
setlocal enabledelayedexpansion

:: Prints IPv4 and IPv6 statistics on Windows

:: Function to get IPv4 ipstats
set "get_ipv4_ipstats="
for /f "tokens=*" %%A in ('netsh interface ipv4 show ipstats') do (
    echo %%A | find "In Receives" >nul
    if !errorlevel! == 0 (
        for /f "tokens=3 delims= " %%B in ("%%A") do (
            set "get_ipv4_ipstats=%%B"
        )
    )
)

:: Function to get IPv6 ipstats
set "get_ipv6_ipstats="
for /f "tokens=*" %%A in ('netsh interface ipv6 show ipstats') do (
    echo %%A | find "In Receives" >nul
    if !errorlevel! == 0 (
        for /f "tokens=3 delims= " %%B in ("%%A") do (
            set "get_ipv6_ipstats=%%B"
        )
    )
)

echo IP statistics (packets)

if "%get_ipv4_ipstats%"=="" set "get_ipv4_ipstats=0"
if "%get_ipv6_ipstats%"=="" set "get_ipv6_ipstats=0"

set /a ipv4=%get_ipv4_ipstats%
set /a ipv6=%get_ipv6_ipstats%


echo IPv4: %ipv4%
echo IPv6: %ipv6%

set /a total=%ipv4%+%ipv6%
echo total: %total%

set /a percentage=100*%ipv6%/%total%
echo percentage IPv6 of total IP traffic: %percentage% %%

endlocal

pause
