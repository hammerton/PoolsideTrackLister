#!C:\Users\Gary\Documents\GitHub\PoolsideTrackLister\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'gunicorn==19.0.0','console_scripts','gunicorn'
__requires__ = 'gunicorn==19.0.0'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('gunicorn==19.0.0', 'console_scripts', 'gunicorn')()
    )
