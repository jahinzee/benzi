"""
benzi: cross-platform audio

Refer to the pyproject.toml file for versioning and other information.

Copyright (C) 2023 jahinzee

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""

from playsound import playsound
import os

from benzi.notifier import get_notifier


def _audio_player(sound_file):
    playsound(sound_file, 0)


def _noop_player():
    pass


def get_player(sound_path):
    if sound_path is None:
        return _noop_player
    if os.path.exists(sound_path):
        return lambda: _audio_player(sound_path)
    else:
        notifier = get_notifier()
        notifier(
            title="Notifications will play silently.",
            message=f"File `{sound_path}` not found.",
        )
        return _noop_player
