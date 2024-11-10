"""
benzi: cross-platform notifications and toasts

Refer to the pyproject.toml file for versioning and other information.

Copyright (C) 2023 jahinzee

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""

import platform
from importlib import resources as ilres
from . import files
import asyncio

if platform.system() == "Windows":
    from windows_toasts import Toast, WindowsToaster, ToastAudio, AudioSource
else:
    from desktop_notifier import DesktopNotifier
    from desktop_notifier.common import Icon


def _windows_notifier(title, message):
    print(f"benzi: {title} {message}")
    toast = Toast()
    toast.text_fields = [f"{title}\n{message}" if message != "" else f"{title}"]
    toast.audio = ToastAudio(AudioSource.IM, looping=False, silent=True)
    WindowsToaster("benzi").show_toast(toast)


def _unix_notifier(title, message):
    print(f"benzi: {title} {message}")
    file_path = str(ilres.files(files) / "icon.png")
    asyncio.run(
        DesktopNotifier("benzi?").send(
            title=title, message=message, icon=Icon(name=file_path)
        )
    )


def get_notifier():
    if platform.system() == "Windows":
        return _windows_notifier
    else:
        return _unix_notifier
