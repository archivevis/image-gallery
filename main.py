import curses
import pixcat
import glob
import sys
import os
import time
from contextlib import contextmanager

@contextmanager
def cd(new_dir):
    prev_dir = os.getcwd()
    os.chdir(new_dir)
    try:
        yield
    finally:
        os.chdir(prev_dir)


def list_images(directory):
    files = []

    with cd(directory):
        files.extend(glob.glob('*.jpg'))
        files.extend(glob.glob('*.png'))

    return files

def get_directory(argument):
    if argument.endswith(".py"):
        return os.getcwd()
    else:
        return argument

class Viewer:
    def __init__(self):
        # Curses stuff
        self.stdscr = curses.initscr()
        curses.cbreak()
        curses.noecho()
        curses.curs_set(0)

        # Photo stuff
        self.directory = get_directory(sys.argv[-1])
        self.dir_files = list_images(self.directory)

        # Screen size
        self.height, self.width = self.stdscr.getmaxyx()
    
    def loop(self):
        try:
            # TODO: figure out why image moves left every other erase/refresh cycle
            while True:
                self.stdscr.erase()
                pixcat.Image("~/Pictures/okayu2.jpg").fit_screen().show()
                self.stdscr.refresh()
                time.sleep(5)
        except KeyboardInterrupt:
            error = False
        finally:
            curses.nocbreak()
            curses.endwin()
            print("See ya soon!")


viewer = Viewer()
viewer.loop()