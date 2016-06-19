#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

from golismero.api.data import Data
from golismero.api.data.resource.url import FolderURL
from golismero.api.data.vulnerability.information_disclosure.url_disclosure \
    import UrlDisclosure
from golismero.api.logger import Logger
from golismero.api.plugin import TestingPlugin


#------------------------------------------------------------------------------
class TestPlugin(TestingPlugin):
    """
    Test plugin.
    """


    #--------------------------------------------------------------------------
    def run(self, info):
        if not isinstance(info, FolderURL):
            raise TypeError("Expected FolderURL, got %r instead" % type(info))

        # Intentionally cause a warning to be shown.
        Logger.log("This is a log message.")
        return UrlDisclosure(info)


    #--------------------------------------------------------------------------
    def get_accepted_types(self):
        return [FolderURL]
