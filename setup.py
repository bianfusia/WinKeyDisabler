from cx_Freeze import setup, Executable

base = None    

executables = [Executable("disabler.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "disable left key",
    options = options,
    version = "0.2",
    description = 'disable left key button through the use of exe',
    executables = executables
)
