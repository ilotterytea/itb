# Copyright (c) 2022 NotDankEnough (ilotterytea)
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from nitb.clients.twitch.TwitchClient import TwitchClient
from nitb.clients.twitch.TwitchIRCIdentity import TwitchIRCIdentity
from nitb.utils.Configuration import getConfig

def run(args: ...) -> None:
    cfg = getConfig("config.ini")

    twitchClient = TwitchClient(
        TwitchIRCIdentity(
            cfg.get("IDENTITY", "USERNAME"),
            cfg.get("IDENTITY", "PASSWORD")
        ),
        cfg.get("CHAT", "CHANNELS").split(',')
    )

    twitchClient.loop()

if __name__ == "__main__":
    run(None)
