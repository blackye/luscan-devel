#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
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


# Fix the module path for the tests.
import sys
import os
from os import path
here = path.split(path.abspath(__file__))[0]
if not here:  # if it fails use cwd instead
    here = path.abspath(os.getcwd())
golismero = path.join(here, "..")
thirdparty_libs = path.join(golismero, "thirdparty_libs")
if path.exists(thirdparty_libs):
    sys.path.insert(0, thirdparty_libs)
    sys.path.insert(0, golismero)


# Imports.
from golismero.api.external import win_to_cygwin_path, cygwin_to_win_path


# Test cases.
win_cygwin_path_cases = (
    ("C:\\Users\\Administrator\\Desktop\\example.txt",
     "/cygdrive/c/Users/Administrator/Desktop/example.txt"),
    ("Z:\\autorun.ini",
     "/cygdrive/z/autorun.ini"),
    ("E:\\folder name with spaces\\file name with a / in the middle.txt",
     "/cygdrive/e/folder name with spaces/file name with a \\/ in the middle.txt"),
)

# Tests the conversion of Windows paths to Cygwin paths.
def test_cygwin_paths():
    print "Testing the conversion of Windows paths to Cygwin paths..."
    for win_path, cygwin_path in win_cygwin_path_cases:
        assert win_to_cygwin_path(win_path) == cygwin_path
        assert cygwin_to_win_path(cygwin_path) == win_path
    assert cygwin_to_win_path(win_to_cygwin_path("c:\\")) == "C:\\"
    assert win_to_cygwin_path(cygwin_to_win_path("/cygdrive/C/")) == "/cygdrive/c/"
    try:
        cygwin_to_win_path("/bin")
        assert False
    except ValueError:
        pass
    try:
        win_to_cygwin_path("test.txt")
        assert False
    except ValueError:
        pass


# Run all tests from the command line.
if __name__ == "__main__":
    test_cygwin_paths()
