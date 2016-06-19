@echo off
rem Run all tests in the current folder.
del _tmp.txt >nul 2>nul
del ..\_tmp.txt >nul 2>nul
del *.log >nul 2> nul
del *.sql >nul 2> nul
for /r %%i in (test_*.bat) do (
    echo %%~ni
    call %%i >> test-out.log 2>> test-err.log
)
for /r %%i in (test_*.py) do (
    echo %%~ni
    python %%i >> test-out.log 2>> test-err.log
)
echo test.py
python test.py >> test-out.log 2>> test-err.log
