#!/usr/bin/env python
# This file is part of Niezapominajka flashcard app
# License: GNU GPL version 3 or later
# Copyright (C) 2025 Wiktor Malinkiewicz

from os import environ
from pathlib import Path

STATE_HOME = None

if 'XDG_STATE_HOME' in environ:
    STATE_HOME = Path(f'{environ["XDG_STATE_HOME"]}/niezapominajka')
else:
    STATE_HOME = Path(f'{environ["HOME"]}/.local/state/niezapominajka')
if not Path.exists(STATE_HOME):
    Path(STATE_HOME).mkdir(parents=True, exist_ok=True)
