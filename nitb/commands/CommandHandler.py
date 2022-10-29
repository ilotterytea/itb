# Copyright (c) 2022 NotDankEnough (ilotterytea)
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from nitb.clients.twitch.TwitchIRCMessage import TwitchIRCMessage
from nitb.clients.twitch.TwitchClient import TwitchClient

from os import listdir
import sys
from importlib import import_module


class TMICommandHandler:
    def __init__(self):
        """
        Handler for Twitch commands.
        """
        self.loaded_commands: dict[str, any] = {}

    def loadAllFromFolder(self, folder_path: str) -> None:
        """
        Load all .py files from folder as commands.

        :param folder_path: Path to the folder
        """
        modules = []

        for file in listdir(folder_path):
            modules.append(file)

        sys.path.append(folder_path)
        print(modules)

        for i in modules:
            i = i[:i.find(".")]
            if i.startswith("_"):
                continue

            self.loadSingle(i)

    def loadSingle(self, file_name: str) -> None:
        """
        Load single .py file as command.

        :param file_name: Path to the file.
        """
        module = import_module(f"{file_name}")
        self.loaded_commands[module.Id] = module

    def call(self, cmdId: str, client: TwitchClient, ctx: TwitchIRCMessage) -> str | None:
        """
        Run the command's function.

        :param cmdId: Command ID.
        :param client: Twitch client.
        :param ctx: Parsed Twitch IRC message.

        :returns: str if command exists, runnable and returns a str. None if command not exists or command returns a None.
        """
        response: str | None = None

        if cmdId in self.loaded_commands:
            mod = self.loaded_commands[cmdId]

            response = mod.run(client, ctx)

        return response
