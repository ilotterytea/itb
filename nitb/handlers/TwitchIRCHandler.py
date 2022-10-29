# Copyright (c) 2022 NotDankEnough (ilotterytea)
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from nitb.utils.ParseMessage import parseMessage

class TwitchIRCHandler:
    def __init__(self, client, command, config):
        """
        Handler for Twitch IRC messages.
        """
        self.client = client
        self.cmd = command
        self.cfg = config

    def process(self, ctx) -> None:
        """
        Process the message.

        :param ctx: Twitch IRC Message.
        """

        # Parse message to commands, options, full message.
        parsed_msg = parseMessage(ctx.message, self.cfg.get("CHAT", "PREFIX"))

        # Call the command and get response:
        response = self.cmd.call(parsed_msg["cmd"], self.client, ctx)

        # If response has what to send:
        if response is not None:
            self.client.sendMessage(ctx.chatName, response)
