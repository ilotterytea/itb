# Copyright (c) 2022 NotDankEnough (ilotterytea)
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from socket import socket
import traceback

from nitb.clients.twitch.TwitchIRCIdentity import TwitchIRCIdentity
from nitb.clients.twitch.TwitchIRCMessage import TwitchIRCMessage
from nitb.clients.twitch.TwitchIRCMessageParser import parseMessage
from nitb.utils.Logger import logging

class TwitchClient:
    def __init__(self, identity: TwitchIRCIdentity | None, channels: list[str]) -> None:
        """
        Create a WebSocket client with Twitch IRC address and connect to it.

        :param identity: Identity of your bot. If None, the client will be anonymous.
        :param channels: Channels that must be joined during initialization.
        """

        self._IDENTITY = identity
        self.channels = channels

        # Twitch's IRC address:
        self._HOST = "irc.twitch.tv"
        self._PORT = 6667

        # Latest IRC message:
        self.LATEST_MESSAGE: TwitchIRCMessage | None = None

        logging.info("Initializing Twitch client...")

        # Creating and connecting to the websocket:
        self._s = socket()
        self._s.connect((self._HOST, self._PORT))

        # Authorizing on the Twitch IRC servers:
        if self._IDENTITY is not None:
            self._s.send(bytes("PASS %s\r\n" % identity.password, "UTF-8"))
            self._s.send(bytes("NICK %s\r\n" % identity.username, "UTF-8"))

        self._s.send(bytes("CAP REQ :twitch.tv/membership\r\n", "UTF-8"))
        self._s.send(bytes("CAP REQ :twitch.tv/commands\r\n", "UTF-8"))
        self._s.send(bytes("CAP REQ :twitch.tv/tags\r\n", "UTF-8"))

        logging.info("Connected and joined the IRC server ({address}:{port})!".format(address=self._HOST,port=self._PORT))

        for channel in self.channels:
            self.joinChannel(channel)

    def getChannels(self) -> list[str]:
        """Get the channels joined by the bot."""
        return self.channels
    
    def joinChannel(self, channel: str) -> None:
        """
        Join to the Twitch chat room.

        :param channel: Valid Twitch username.
        """
        if channel in self.channels:
            return
        
        self._s.send(bytes("JOIN #%s\r\n" % channel, "UTF-8"))
        self.channels.append(channel)
        logging.info("JOIN #{channel}".format(channel=channel))

    def partChannel(self, channel: str) -> None:
        """
        Part from the Twitch chat room.

        :param channel: Valid Twitch username.
        """
        if channel not in self.channels:
            return
        
        self._s.send(bytes("PART #%s\r\n" % channel, "UTF-8"))
        del self.channels[self.channels.index(channel)]
        logging.info("PART #{channel}".format(channel=channel))

    def sendMessage(self, channel: str, message: str) -> None:
        """
        Send message to the Twitch chat room.

        :param channel: Valid Twitch username.
        :param message: Message.
        """
        if self._IDENTITY is None:
            logging.warn("Can't send a message! Reason: Twitch IRC Identity is None.")
            return

        self._s.send(bytes("PRIVMSG #{channel} :{message}\r\n".format(channel=channel, message=message), "UTF-8"))
        logging.info("PRIVMSG #{channel} :{msg}".format(channel=channel, msg=message))

    def close(self) -> None:
        """
        Close the WebSocket connection.
        """

        self._s.close()
        logging.info("The WebSocket connection was closed!")

    def loop(self, handler) -> None:
        """
        Starts processing all Twitch messages in a whileloop. At the same time, starts handling commands from the chat.
        Must be placed at the very end of your script if you want a working bot.

        :except KeyboardInterrupt: Use your keyboard and CTRL+C to escape from while-loop.
        """
        read_buf: str = ""

        while True:
            try:
                read_buf = read_buf + self._s.recv(1024).decode("UTF-8")
            except KeyboardInterrupt:
                self._s.close()
                raise
            except:
                logging.error(traceback.format_exc())

            temp = str.split(read_buf, "\r\n")
            read_buf = temp.pop()

            for line in temp:
                match line.split(' ')[0]:
                    # Response PONG on Twitch's PING:
                    case "PING":
                        self._s.send(bytes("PONG %s\rp\n" % line[1], "UTF-8"))
                        logging.debug("Pong! Sorry, Twitch just sent PING to me.")

                match line.split(' ')[2]:
                    case "PRIVMSG":
                        # Call the command handler:
                        self.LATEST_MESSAGE = parseMessage(line)
                        handler.process(self.LATEST_MESSAGE)
