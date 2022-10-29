# Copyright (c) 2022 NotDankEnough (ilotterytea)
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from nitb.clients.twitch.TwitchClient import TwitchClient
from nitb.clients.twitch.TwitchIRCIdentity import TwitchIRCIdentity
from nitb.utils.Configuration import getConfig
from nitb.utils.ParseArguments import parseArguments


def run(args: any) -> None:
    # Bot configuration:
    cfg = getConfig(args.config)

    twitchClient = TwitchClient(
        TwitchIRCIdentity(
            cfg.get("IDENTITY", "USERNAME"),
            cfg.get("IDENTITY", "PASSWORD")
        ),
        cfg.get("CHAT", "CHANNELS").split(',')
    )

    twitchClient.loop()

if __name__ == "__main__":
    # Parse CLI arguments and run the bot:
    run(parseArguments())
