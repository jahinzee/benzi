#!/usr/bin/env python

# benzi: big ben on your desktop.
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


def notify(notifier, logs, sound):
    if sound is not None:
        playsound(sound, 0)
    logs.info(f"INFO: it is {datetime.now():%H:%M}.")
    notifier.send_sync(title=f"It is {datetime.now():%H:%M}.",
                       message="",
                       icon=(""))


def notify_sound_error(notifier, logs, sound_path):
    logs.warning(f"WARNING: file '{sound_path}' not found.")
    notifier.send_sync(title=f"File '{sound_path}' not found.",
                       message="Notifications will play silently.",
                       icon=(""))


def get_sound(notifier, logs, sound_path):
    if sound_path is None:
        return None
    if path.exists(sound_path):
        return sound_path
    else:
        notify_sound_error(notifier, logs, sound_path)
        return None


def get_args():
    parser = argparse.ArgumentParser(description="big ben on your desktop.")
    parser.add_argument('-s', '--sound', type=str,
                        help="specify a sound file to play on the hour")
    return parser.parse_args()


def get_logs():
    logging.basicConfig(format='%(message)s')
    return logging.getLogger(__name__)


def main():
    args = get_args()
    logs = get_logs()
    notifier = DesktopNotifier("benzi")
    sound = get_sound(notifier, logs, args.sound)
    schedule.every().hour.at(":00").do(lambda: notify(notifier, logs, sound))
    try:
        while True:
            schedule.run_pending()
            time.sleep(.1)
    except KeyboardInterrupt:
        logs.error('SIGINT received, exiting...')
        exit(1)


if __name__ == "__main__":
    main()
