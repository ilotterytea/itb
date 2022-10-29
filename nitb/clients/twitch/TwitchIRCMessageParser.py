# Copyright (c) 2022 NotDankEnough (ilotterytea)
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from nitb.clients.twitch.TwitchIRCMessage import TwitchIRCMessage


def parseMessage(raw_message: str) -> TwitchIRCMessage:
    """
    Parse a raw message that was sent by Twitch.
    :param raw_message: Raw message. It should look like this: @badge-info=;badges=;color=#00FF7F;...
    :return: Baked TwitchIRCMessage
    """

    # Not filled TwitchIRCMessage:
    msg = TwitchIRCMessage(
        badgeInfo=[], badges={}, color="", displayName="",
        userName="", userId=0, userType="", isModerator=False,
        isSubscriber=False, isTurbo=False, chatId=0, chatName="",
        messageId="", tmiSentTs=0, emotes={}, flags="",
        firstMessage=False, returningChatter=False,
        message="", ircType=""
    )

    tmp = raw_message.split(' ')

    # Message parameters, e.g. "@badge-info=;badges=..."
    msgParams = [p for p in tmp[0].split(';')]

    # Setting the message parameters:
    for option in msgParams:
        row: list[str | None] = option.split('=')

        # If key doesn't have any values, add the None value:
        if len(row) < 2:
            row[1] = None

        match row[0]:
            case "@badge-info": msg.badgeInfo = row[1]
            case "badges":
                d: dict[str, bool] = {}

                # Transforming into a friendly format, e.g. {"moderator": True} instead of "moderator/1"
                for badge in row[1].split(','):
                    bb = badge.split('/')
                    d[bb[0]] = bool(int(bb[1]))

                msg.badges = d
            case "color": msg.color = row[1]
            case "display-name": msg.displayName = row[1]
            case "emotes": msg.emotes = row[1]
            case "first-msg": msg.firstMessage = bool(int(row[1]))
            case "flags": msg.flags = row[1]
            case "id": msg.messageId = row[1]
            case "mod": msg.isModerator = bool(int(row[1]))
            case "returning-chatter": msg.returningChatter = bool(int(row[1]))
            case "room-id": msg.chatId = int(row[1])
            case "subscriber": msg.isSubscriber = bool(int(row[1]))
            case "tmi-sent-ts": msg.tmiSentTs = int(row[1])
            case "turbo": msg.isTurbo = bool(int(row[1]))
            case "user-id": msg.userId = int(row[1])
            case "user-type": msg.userType = row[1]

    # Setting a sender's username:
    msg.userName = tmp[1][1:].split('!')[0]

    # Setting the type of IRC message:
    msg.ircType = tmp[2]

    # Setting the room name without '#':
    msg.chatName = tmp[3][1:]

    # Full chat message:
    msg.message = ' '.join(tmp[4:])[1:]

    return msg
