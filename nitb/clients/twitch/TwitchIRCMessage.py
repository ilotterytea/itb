# Copyright (c) 2022 NotDankEnough (ilotterytea)
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from dataclasses import dataclass

@dataclass
class TwitchIRCMessage:
    """
    Data of received Twitch message.
    """

    badgeInfo: list[str]
    badges: dict[str, bool]
    color: str

    displayName: str
    userName: str
    userId: int
    userType: str
    isModerator: bool
    isSubscriber: bool
    isTurbo: bool

    chatId: int
    chatName: str

    messageId: str
    tmiSentTs: int
    emotes: dict
    flags: str

    firstMessage: bool
    returningChatter: bool
