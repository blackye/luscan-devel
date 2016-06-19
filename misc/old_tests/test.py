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


# Standard imports.
import os
from os import path
import sys
import time


# Fix the module path for the tests.
here = path.split(path.abspath(__file__))[0]
if not here:  # if it fails use cwd instead
    here = path.abspath(os.getcwd())
golismero = path.join(here, "..")
thirdparty_libs = path.join(golismero, "thirdparty_libs")
if path.exists(thirdparty_libs):
    sys.path.insert(0, thirdparty_libs)
    sys.path.insert(0, golismero)


# GoLismero imports.
from golismero.api.data import Data
from golismero.api.plugin import STAGES
from golismero.api.text.text_utils import generate_random_string
from golismero.common import OrchestratorConfig, AuditConfig
from golismero.database.auditdb import AuditDB
from golismero.main.launcher import run
from golismero.managers.pluginmanager import PluginManager


# Test GoLismero.
def test():

    config = OrchestratorConfig()
    config.from_dictionary({
        "plugins_folder": path.abspath(path.join(here, "plugin_tests")),
        "ui_mode": "test",
    })

    audit = AuditConfig()
    audit.from_dictionary({
        "targets": ["http://www.example.com/folder/subfolder/index.html",],
        "reports": ["-",],
        "audit_db": "",
    })
    ##audit.plugin_load_overrides = [(True, "recon/test")]  # XXX DEBUG shorter run

    try:
        print "Launching GoLismero..."
        print
        t1 = time.time()
        code = run(config, audit)
        t2 = time.time()
        print
        print "GoLismero ran for %f seconds" % (t2 - t1)
        print
        assert code == 0

        print "Validating the audit database..."
        print
        validate(audit)

    finally:
        print "Cleaning up..."
        print
        try:
            os.unlink("%s.db" % audit.audit_name)
        except Exception:
            pass
    print "Done!"


# Validate the audit database.
def validate(audit):
    disk = AuditDB(audit)
    try:

        # Make sure all objects completed all stages.
        for stage in sorted(STAGES.values()):
            assert disk.get_pending_data(stage) == set()



    finally:
        disk.close()


# Run all tests from the command line.
if __name__ == "__main__":
    test()
