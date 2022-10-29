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

    # Info about badges. (?) (Twitch sending just an empty string, I don't know what is this exactly)
    badgeInfo: list[str]
    # Sender's equipped badges.
    badges: dict[str, bool]
    # Sender's color.
    color: str

    # Sender's display username. It can be hieroglyphics or with some uppercase letters.
    displayName: str

    # Sender's name. Always in lowercase.
    userName: str

    # Sender's ID.
    userId: int

    # Sender's type. Moderator, user, staff, etc.
    userType: str

    # Is sender a moderator in this chat room?
    isModerator: bool

    # Is sender a subscriber in this chat room?
    isSubscriber: bool

    # Is sender a turbo subscriber?
    isTurbo: bool


    # Chat room's ID.
    chatId: int

    # Chat room's name.
    chatName: str

    # Sent message.
    message: str

    # Message's ID
    messageId: str

    tmiSentTs: int
    emotes: dict
    flags: str

    # Did sender just send their first message?
    firstMessage: bool

    returningChatter: bool

    # Type of IRC message: ROOMSTATE, PRIVMSG, etc. (Parameter for nerds)
    ircType: str
