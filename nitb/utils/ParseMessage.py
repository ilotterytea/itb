# Copyright (c) 2022 NotDankEnough (ilotterytea)
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT


def parseMessage(raw_message: str, prefix: str) -> dict[str, str | None]:
    """
    Parse the message.

    :param raw_message: Raw message, e.g. "!massping -c hello world!".
    :param prefix: Command prefix.
    :returns: Dictionary, e.g. {cmd: "!massping", opt: ["-c"], "msg": "hello world!"}
    """

    command: str | None = None
    options: list[str] | None = None

    s = raw_message.split(' ')

    if raw_message.startswith(prefix):
        # Set the command:
        command = s[0][len(prefix):]
        del s[0]

    for word in s:
        # Parse option:
        if word.startswith('-'):
            if options is None:
                options = []

            options.append(word)

            del s[s.index(word)]

    return {
        "cmd": command,
        "opt": options,
        "msg": ' '.join(s)
    }
