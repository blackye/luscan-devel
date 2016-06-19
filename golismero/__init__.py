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

__all__ = [

    # Metadata
    "__author__",
    "__copyright__",
    "__credits__",
    "__email__",
    "__version__",

    # Banner
    "get_banner",
    "show_banner",
]


#------------------------------------------------------------------------------
# Metadata

__author__     = "GoLismero project team"
__copyright__  = "Copyright (C) 2011-2014 GoLismero Project"
__credits__    = ["GoLismero Project Team"]
__email__      = "contact@golismero-project.com"
__version__    = "2.0.0b6"


#------------------------------------------------------------------------------
def get_banner():
    """
    :returns: The program banner.
    :rtype: str
    """
    banner_lines = [
        "GoLismero %s, The Web Knife" % __version__,
        __copyright__,
        "",
        "Contact: " + __email__,
    ]
    width = max(len(line) for line in banner_lines)
    banner = "\n/-" + ("-" * width) + "-\\\n"
    for line in banner_lines:
        banner += "| " + line + (" " * (width - len(line))) + " |\n"
    banner += "\\-" + ("-" * width) + "-/\n"
    return banner


#------------------------------------------------------------------------------
def show_banner():
    """
    Prints the program banner.
    """
    print get_banner()
