#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Internally used submodule that contains runtime patches
to the standard multiprocessing library.

.. warning: Do not import this submodule in your code!
            This is only meant to be imported from the
            processmanager submodule!
"""

__license__ = """
GoLismero 2.0 - The web knife - Copyright (C) 2011-2014

Golismero project site: https://github.com/golismero
Golismero project mail: contact@golismero-project.com

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""

__all__ = []


#------------------------------------------------------------------------------
# This patches the multiprocessing module in runtime to prevent bogus error
# messages to be shown when Control-C is pressed by the user.
#------------------------------------------------------------------------------


import sys
from os import path
from signal import signal, SIGINT

# Signal handler that kills the current process.
# This should trigger a chain reaction when Control-C is pressed.
def __suicide(signum, frame):
    exit(1)
signal(SIGINT, __suicide)

# Mimics a file object well enough to suppress print messages.
# Also faster than opening a file descriptor for /dev/null.
class __FakeFile(object):
    def write(self, s):
        pass
    def flush(self):
        pass
    def close(self):
        pass

# Get the original values for stdout and stderr.
__orig_stdout, __orig_stderr = sys.stdout, sys.stderr

# Our wrapper to the bootstrap function.
# It replaces stdout and stderr with a fake file object,
# and sets a signal handler to commit suicide on Control-C.
def __patched_bootstrap(self):
    signal(SIGINT, __suicide)
    stdout, stderr = sys.stdout, sys.stderr
    sys.stdout, sys.stderr = __FakeFile(), __FakeFile()
    try:
        return __original_bootstrap(self)
    finally:
        sys.stdout, sys.stderr = stdout, stderr

if sys.platform == "win32":

    # Wraps around get_command_line()
    # to set our own main() function in new processes.
    def __patched_get_command_line():

        # Calculate the command line that would normally be used.
        args = _original_get_command_line()

        # Make sure everything looks like we expect it.
        # A new version of the multiprocessing module might break this,
        # but since Python 2.7 is in bugfix mode, this is unlikely.
        # We're checking anyway, just in case.
        assert args[-3] == '-c', \
            "internal error, are you sure this is Python 2.7?"
        assert args[-2] == 'from multiprocessing.forking import main; main()',\
            "internal error, are you sure this is Python 2.7?"
        assert args[-1] == '--multiprocessing-fork', \
            "internal error, are you sure this is Python 2.7?"

        # Calculate the new startup code to run on new processes.
        # It calls our main function instead of the real one.
        here = path.abspath(path.join(path.split(__file__)[0], "..", ".."))
        tpl  = path.join(here, "thirdparty_libs")
        code = "import sys; "
        if path.exists(tpl):
            ehere = here.replace("'", "\\'").replace('"', '\\x%.2x' % ord('"'))
            etpl  = tpl.replace("'", "\\'").replace('"', '\\x%.2x' % ord('"'))
            code += "here = '%s'; " % ehere
            code += "sys.path.insert(0, here); "
            code += "tpl = '%s'; " % etpl
            code += "sys.path.insert(0, tpl); "
        code += "from golismero.patches.mp import main; main()"

        # Patch the command line and return it.
        args[-2] = code
        return args

    # Our wrapper works around a sanity check of multiprocessing.
    # At one point it checks the main module wasn't already loaded.
    # However the check fails because our launch script (golismero.py)
    # results in the same module name as ourselves (golismero/__init__.py).
    def __patched_prepare(data):
        golismero = sys.modules["golismero"]
        try:
            del sys.modules["golismero"]
            return _original_prepare(data)
        finally:
            sys.modules["golismero"] = golismero

    # Our wrapper to the main() function of new processes.
    # It replaces stdout and stderr with a fake file object.
    def main():
        from multiprocessing.forking import main as original_main
        from multiprocessing import Process
        if Process._bootstrap.__name__ != "__patched_bootstrap":
            global __original_bootstrap
            __original_bootstrap = Process._bootstrap
            Process._bootstrap = __patched_bootstrap
        stdout, stderr = sys.stdout, sys.stderr
        sys.stdout, sys.stderr = __FakeFile(), __FakeFile()
        try:
            original_main()
        finally:
            sys.stdout, sys.stderr = stdout, stderr

if __name__ != "__parents_main__" and __name__ != "__main__":

    # Patch the bootstrap function for child processes.
    from multiprocessing import Process
    if Process._bootstrap.__name__ != "__patched_bootstrap":
        __original_bootstrap = Process._bootstrap
        Process._bootstrap = __patched_bootstrap

        if sys.platform == "win32":
            from multiprocessing import forking

            # Patch the function that calculates
            # the command line for child processes.
            from multiprocessing.forking import get_command_line as \
                _original_get_command_line
            forking.get_command_line = __patched_get_command_line

            # Patch the function that prepares the data for child processes.
            from multiprocessing.forking import prepare as _original_prepare
            forking.prepare = __patched_prepare

# Undoes the patches. This is required to be able to reload GoLismero.
def undo():
    Process._bootstrap = __original_bootstrap
    if sys.platform == "win32":
        forking.get_command_line = _original_get_command_line
        forking.prepare = _original_prepare
    if __orig_stdout is not None and hasattr(sys.stdout, "__class__") and \
                    sys.stdout.__class__.__name__ == __FakeFile.__name__:
        sys.stdout = __orig_stdout
    if __orig_stderr is not None and hasattr(sys.stderr, "__class__") and \
                    sys.stderr.__class__.__name__ == __FakeFile.__name__:
        sys.stderr = __orig_stderr
