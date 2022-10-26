# Copyright (c) 2022 NotDankEnough (ilotterytea)
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from configparser import ConfigParser
from os.path import exists
from nitb.utils.Logger import logging

def getConfig(file_path: str) -> ConfigParser:
    """
    Get the bot configuration. Create a new one, if not exists.
    :return: ConfigParser with values.
    """

    cfg = ConfigParser()
    shouldRewrite = False

    # Load current configuration if exists:
    if exists(file_path):
        logging.info("Found the configuration file ({path})!".format(path=file_path))
        cfg.read(file_path)

    # Section check:
    if cfg.has_section("IDENTITY") is False: cfg.add_section("IDENTITY"); shouldRewrite = True
    if cfg.has_section("CHAT") is False: cfg.add_section("CHAT"); shouldRewrite = True

    # Identity options check:
    if cfg.has_option("IDENTITY", "USERNAME") is False: cfg.set("IDENTITY", "USERNAME", "BOT_USERNAME_HERE_PLEASE"); shouldRewrite = True
    if cfg.has_option("IDENTITY", "PASSWORD") is False: cfg.set("IDENTITY", "PASSWORD", "oauth:BOT_OAUTH_TOKEN"); shouldRewrite = True

    # Chat options check:
    if cfg.has_option("CHAT", "CHANNELS") is False: cfg.set("CHAT", "CHANNELS", "someuser,someone"); shouldRewrite = True

    # Overwrite the configuration file if some options are missing, or save the file if it doesn't exist:
    if exists(file_path) is False or shouldRewrite:
        with open(file_path, "w") as file:
            cfg.write(file)
            file.close()

        print("Sorry, your configuration file was just created/overwritten. Please, put the values in the new fields so that the bot works correctly!")
        logging.error("Sorry, your configuration file was just created/overwritten. Please, put the values in the new fields so that the bot works correctly!")
        exit(1)

    return cfg
