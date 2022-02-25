pushd %~dp0

copy /Y settings_aida64_max_frequency.py settings.py

:: You may also replace this with `python` or `python3X` if you are having issues
py main.py

popd
