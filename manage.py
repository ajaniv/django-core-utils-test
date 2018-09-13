#!/usr/bin/env python
import os
import sys
from six import raise_from
msg = ("Couldn't import Django. Are you sure it's installed and "
       "available on your PYTHONPATH environment variable? Did you "
       "forget to activate a virtual environment?")

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                          "django_core_utils_test.settings")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise_from(ImportError(msg), exc)
    execute_from_command_line(sys.argv)
