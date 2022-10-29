# Copyright (c) 2022 NotDankEnough (ilotterytea)
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from argparse import ArgumentParser, Namespace


def parseArguments() -> Namespace:
    """
    Parse command line arguments.
    """
    parser = ArgumentParser(
        description="Start the bot program."
    )

    parser.add_argument(
        "--config", "-c",
        default="config.ini",
        help="Specify with which configuration file to load the bot. (Default: config.ini)"
    )

    return parser.parse_args()
