import inspect 
import os
import sys

print("---------------- WPN_GENERATOR PACKAGE INITIALIZING ---------------------")
src_file_path = inspect.getfile(lambda: None)

PYTHON_ROOT = os.path.split(src_file_path)[0] #WPN_GENERATOR/python3.7libs
PACKAGE_ROOT = os.path.split(PYTHON_ROOT)[0]  #WPN_GENERATOR
VENV_ROOT = f"{PYTHON_ROOT}/WPN_GENERATOR_PY/venv/Lib/site-packages"

if VENV_ROOT not in sys.path:
    sys.path.append(VENV_ROOT)
    print(f"Appending Venv to sys_path: {VENV_ROOT}")


""" INIT ENV VARS HERE"""
print("---------------- WPN_GENERATOR PACKAGE INITIALIZED ---------------------")