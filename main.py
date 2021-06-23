import curses
import pixcat
import glob
import sys
import os
from contextlib import contextmanager

@contextmanager
def cd(new_dir):
    prev_dir = os.getcwd()
    os.chdir(new_dir)
    print("going to", os.getcwd())
    try:
        yield
    finally:
        os.chdir(prev_dir)
        print("back to", os.getcwd())


def list_images(directory):
    files = []

    with cd(directory):
        files.extend(glob.glob('*.jpg'))
        files.extend(glob.glob('*.png'))

    return files

class Gallery:
    def __init__(self):
        # Curses stuff
        self.stdscr = curses.initscr()
        curses.cbreak()
        curses.noecho()
        curses.curs_set(0)

        # Photo stuff
        self.directory = sys.argv[-1]
        self.dir_files = list_images(self.directory)
