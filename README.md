# WinKeyDisabler

## Adding to startup
- You can move the vbs script to this location to run script at startup in background
```bash
C:\Users\Benjamin\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
```

## Making ```disabler.py``` into exe
- you will first have to ```cd``` to the location of your ```setup.py``` then run the following:
```bash
python setup.py build
```
- you will also how to redirect the batch script to launch your ```.exe``` instead.

## Note
- This script on disable left arrow button, to disable other buttons your may refer to this [documentation](https://pypi.org/project/keyboard/).
