# Copyright (c) 2022 NotDankEnough (ilotterytea)
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from requests import get


class TwitchUtils:
    """
    Small utilities that related to Twitch.
    """

    @classmethod
    def getChatters(cls, channel_name: str) -> dict:
        """
        Get list of chatters.

        :param channel_name: Valid channel name.
        :returns: Dictionary of chatters.
        """

        return get(
            url=f"https://tmi.twitch.tv/group/user/{channel_name}/chatters"
        ).json()
