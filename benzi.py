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
from datetime import datetime


def notify(notifier):
    notifier.send_sync(title=f"It is {datetime.now():%H:%M}.",
                       message="",
                       icon=(""))


def main():
    notifier = DesktopNotifier("benzi")
    schedule.every().hour.at(":00").do(lambda: notify(notifier))
    while True:
        schedule.run_pending()
        time.sleep(.1)


if __name__ == "__main__":
    main()
