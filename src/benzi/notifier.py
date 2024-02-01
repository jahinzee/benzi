"""
benzi: cross-platform notifications and toasts

Refer to the pyproject.toml file for versioning and other information.

Copyright (C) 2023 jahinzee

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""

import platform

if platform.system() == "Windows":
    from windows_toasts import Toast, WindowsToaster, ToastAudio, AudioSource
else:
    from desktop_notifier import DesktopNotifier


def _windows_notifier(title, message):
    print(f"benzi: {title} {message}")
    toast = Toast()
    toast.text_fields = [f"{title}\n{message}" if message != "" else f"{title}"]
    toast.audio = ToastAudio(AudioSource.IM, looping=False, silent=True)
    WindowsToaster("benzi").show_toast(toast)


def _unix_notifier(title, message):
    print(f"benzi: {title} {message}")
    DesktopNotifier("benzi").send_sync(title=title, message=message, icon=(""))


def get_notifier():
    if platform.system() == "Windows":
        return _windows_notifier
    else:
        return _unix_notifier
