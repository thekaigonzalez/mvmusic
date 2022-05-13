#!/usr/bin/env python3
import os

import sys
import glob
import shutil
import pathlib
import termcolor as tc


def move_music_from(path):
    if not pathlib.Path(os.path.expanduser(path)).exists():
        tc.cprint("error: Downloads directory not found")
        exit(-1)
    tc.cprint("Found downloads, copying files...", "blue")
    for i in glob.glob(os.path.expanduser(path + "/*.mp3")):
        shutil.copy(i, os.path.expanduser("~/Music/"))
        tc.cprint(f"FILE: {i}", "yellow")


move_music_from("~/Downloads")
