# Copyright (c) 2022 NotDankEnough (ilotterytea)
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from enum import Enum


class Permissions(Enum):
    """
    Permissions to access to run the command.
    """

    SUSPENDED = -1
    """Suspended chatter. Banned from USING the bot, not from chatting."""

    USER = 0
    """Average chatter."""

    VIP = 1
    """VIP chatter."""

    MOD = 2
    """Moderator."""

    # Broadcaster.
    BROADCASTER = 3
    """Broadcaster."""

    SUPERUSER = 99
    """Superuser. Can do anything with bot. Give out this role wisely."""
