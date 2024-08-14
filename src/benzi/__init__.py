"""
benzi: main script

Refer to the pyproject.toml file for versioning and other information.

Copyright (C) 2023 jahinzee

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""

import schedule
import time
import argparse
from datetime import datetime

from benzi.notifier import get_notifier
from benzi.player import get_player


def chime(notifier, player):
    player()
    notifier(title=f"It is {datetime.now():%H:%M}.", message="")


def get_args():
    parser = argparse.ArgumentParser(
        description="A cross-platform utility that sends you a desktop notification on the hour, every hour."
    )
    parser.add_argument(
        "-s", "--sound", type=str, help="specify a sound file to play on the hour"
    )
    parser.add_argument(
        "-t",
        "--test",
        action="store_true",
        help="send a test notification on launch and exit",
    )
    return parser.parse_args()


def main():
    args = get_args()
    notifier = get_notifier()
    player = get_player(args.sound)
    chime_lambda = lambda: chime(notifier, player)  # noqa: E731
    if args.test:
        chime_lambda()
        exit(0)
    schedule.every().hour.at(":00").do(chime_lambda)
    try:
        while True:
            schedule.run_pending()
            time.sleep(0.1)
    except KeyboardInterrupt:
        exit(0)


if __name__ == "__main__":
    main()
