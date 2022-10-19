#!E:\Users\Jason\Documents\houdini18.5\python3.7libs\WPN_GENERATOR_PY\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'psd-tools==1.9.18','console_scripts','psd-tools'
__requires__ = 'psd-tools==1.9.18'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('psd-tools==1.9.18', 'console_scripts', 'psd-tools')()
    )
