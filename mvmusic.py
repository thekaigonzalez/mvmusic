#!/usr/bin/env python3
import os

import sys
import glob
import shutil

def move_music_from(path):
	for i in glob.glob(os.path.expanduser(path + "/*.mp3")):
		shutil.copy(i, os.path.expanduser("~/Music/"))

move_music_from("~/Downloads")
