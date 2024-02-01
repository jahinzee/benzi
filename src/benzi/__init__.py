#!/usr/bin/env python

# benzi: big ben on your desktop.
#
# Refer to the pyproject.toml file for versioning and other information.
#
# Copyright (C) 2023 jahinzee
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.


from desktop_notifier import DesktopNotifier
import schedule
import time
from playsound import playsound
from os import path
from datetime import datetime
import argparse
import logging


def notify(notifier, title, message):
    print(f"benzi: {title} {message}")
    notifier.send_sync(title=title, message=message, icon=(""))


def chime(notifier, sound):
    if sound is not None:
        playsound(sound, 0)
    notify(notifier, title=f"It is {datetime.now():%H:%M}.", message="")


def get_sound(notifier, sound_path):
    if sound_path is None:
        return None
    if path.exists(sound_path):
        return sound_path
    else:
        notify(
            notifier,
            title=f"File {sound_path} not found.",
            message="Notifications will play silently.",
        )
        return None


def get_args():
    parser = argparse.ArgumentParser(description="big ben on your desktop.")
    parser.add_argument(
        "-s", "--sound", type=str, help="specify a sound file to play on the hour"
    )
    parser.add_argument(
        "-t", "--test", action="store_true", help="send a test notification on launch and exit"
    )
    return parser.parse_args()


def main():
    args = get_args()
    notifier = DesktopNotifier("benzi")
    sound = get_sound(notifier, args.sound)
    chime_lambda = lambda: chime(notifier, sound)
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