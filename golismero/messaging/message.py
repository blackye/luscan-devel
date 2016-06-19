#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Messages send information, vulnerabilities, resources and internal control
events between the different components of GoLismero.

They may be shared locally (console run mode) or serialized and sent across
the network (cloud run modes).
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

__all__ = ["Message"]

from .codes import *  # noqa

from time import time


#------------------------------------------------------------------------------
class Message (object):
    """
    Messages send information, vulnerabilities, resources and internal control
    events between the different components of GoLismero.

    They may be shared locally (console run mode) or serialized and sent across
    the network (cloud run modes).
    """


    #--------------------------------------------------------------------------
    def __init__(self, message_type = 0,
                       message_code = 0,
                       message_info = None,
                         audit_name = None,
                          plugin_id = None,
                       ack_identity = None,
                           priority = MessagePriority.MSG_PRIORITY_MEDIUM):
        """
        :param message_type: Message type. Must be one of the constants from MessageType.
        :type mesage_type: int

        :param message_code: Message code. Must be one of the constants from MessageCode.
        :type message_code: int

        :param message_info: The payload of the message. Its type depends on the message type and code.
        :type message_info: \\*

        :param audit_name: Name of the audit this message belongs to, if any.
        :type audit_name: str | None

        :param plugin_id: ID of the plugin that sent this message, if any.
        :type plugin_id: str | None

        :param ack_identity: Identity hash of the current input data, or None if not running a plugin.
        :type ack_identity: str | None

        :param priority: Priority level. Must be one of the constants from MessagePriority.
        :type priority: int
        """

        # Validate the argument types.
        if type(message_type) != int:
            raise TypeError("Expected int, got %r instead" % type(message_type))
        if type(message_code) != int:
            raise TypeError("Expected int, got %r instead" % type(message_code))
        if audit_name is not None and type(audit_name) not in (str, unicode):
            raise TypeError("Expected int, got %r instead" % type(audit_name))
        if plugin_id is not None and type(plugin_id) not in (str, unicode):
            raise TypeError("Expected int, got %r instead" % type(plugin_id))
        if ack_identity is not None and type(ack_identity) != str:
            raise TypeError("Expected str, got %r instead" % type(ack_identity))
        if type(priority) != int:
            raise TypeError("Expected int, got %r instead" % type(priority))

        # Validate the codes.
        if message_type not in MSG_TYPES:
            raise ValueError("Invalid message type: %d" % message_type)
        if message_type == MessageType.MSG_TYPE_CONTROL:
            if not message_code in MSG_CONTROL_CODES:
                raise ValueError("Invalid control message code: %d" % message_code)
        elif message_type == MessageType.MSG_TYPE_RPC:
            if not message_code in MSG_RPC_CODES:
                raise ValueError("Invalid RPC message code: %d" % message_code)
        elif message_type == MessageType.MSG_TYPE_STATUS:
            if not message_code in MSG_STATUS_CODES:
                raise ValueError("Invalid status message code: %d" % message_code)
        elif message_type == MessageType.MSG_TYPE_DATA:
            if not message_code in MSG_DATA_CODES:
                raise ValueError("Invalid data message code: %d" % message_code)
        if priority not in MSG_PRIORITIES:
            raise ValueError("Invalid priority level: %d" % priority)

        # Build the message object.
        self.__message_type = message_type
        self.__message_code = message_code
        self.__message_info = message_info
        self.__audit_name   = audit_name
        self.__plugin_id    = plugin_id
        self.__ack_identity = ack_identity
        self.__priority     = priority
        self.__timestamp    = time()


    #--------------------------------------------------------------------------
    @property
    def message_type(self):
        """
        :returns: Message type. Must be one of the constants from MessageType.
        :rtype: int
        """
        return self.__message_type

    @property
    def message_code(self):
        """
        :returns: Message code. Must be one of the constants from MessageCode.
        :rtype: int
        """
        return self.__message_code

    @property
    def message_info(self):
        """
        :returns: The payload of the message. Its type depends on the message type and code.
        :rtype: \\*
        """
        return self.__message_info

    @property
    def audit_name(self):
        """
        :returns: Name of the audit this message belongs to, if any.
        :rtype: str | None
        """
        return self.__audit_name

    @property
    def plugin_id(self):
        """
        :returns: ID of the plugin that sent this message, if any.
        :rtype: str | None
        """
        return self.__plugin_id

    @property
    def ack_identity(self):
        """"
        :returns: Identity hash of the current input data, or None if not running a plugin.
        :rtype: str | None
        """
        return self.__ack_identity

    @property
    def priority(self):
        """
        :returns: Priority level. Must be one of the constants from MessagePriority.
        :rtype: int
        """
        return self.__priority

    @property
    def timestamp(self):
        """
        :returns: POSIX timestamp for this message.
        :rtype: int
        """
        return self.__timestamp


    #--------------------------------------------------------------------------
    @property
    def is_ack(self):
        """
        :returns: True if this message is an ACK, False otherwise.
        :rtype: bool
        """
        return (self.message_type == MessageType.MSG_TYPE_CONTROL and
                self.message_code == MessageCode.MSG_CONTROL_ACK)


    #--------------------------------------------------------------------------
    def __repr__(self):
        s  = (
            "<Message timestamp=%r, type=%s, code=%s, audit=%r, plugin=%r, "
            "ack=%r, info=%r>"
        )
        s %= (
            self.timestamp,
            MessageType.get_name_from_value(self.message_type),
            MessageCode.get_name_from_value_and_type(self.message_code,
                                                     self.message_type),
            self.audit_name,
            self.plugin_id,
            self.ack_identity,
            self.message_info,
        )
        return s
