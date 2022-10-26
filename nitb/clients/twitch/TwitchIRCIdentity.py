# Copyright (c) 2022 NotDankEnough (ilotterytea)
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from dataclasses import dataclass

@dataclass
class TwitchIRCIdentity:
    """
    A data class to identify yourself to Twitch IRC.
    """
    username: str
    password: str
