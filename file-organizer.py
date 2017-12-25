from os import listdir, makedirs
from os.path import isfile, expanduser
from shutil import move
from datetime import datetime
import re


def list_files(tdir):
    """Returns files in the passed directory, ignoring folders"""
    return [f for f in listdir(tdir) if isfile(tdir + f)]


def filter_files(pattern, file_names):
    """Filters file names based on the passed regex and list of file names"""
    p = re.compile(pattern)
    return [p.match(f) for f in file_names if p.match(f) is not None]


def move_file(filename, src, dst):
    """A file move, of filename in src to dst, creating dst if needed"""
    makedirs(dst, exist_ok=True)
    move(src + filename, dst + filename)


def main():
    now = datetime.now()
    print(now.strftime("%d-%m-%Y %H:%M:%S | Running file organizer..."))
    target_dir = expanduser('~') + '/Documents/'
    file_names = list_files(target_dir)
    filtered_matches = filter_files('^\w{3}\d{3}', file_names)
    print("Found files: " + ', '.join([m.string for m in filtered_matches]))
    for f in filtered_matches:
        print(
            'Moving ' +
            f.string +
            ' from ' +
            target_dir +
            ' to ' +
            target_dir +
            f.group() +
            '/')
        move_file(f.string, target_dir, target_dir + f.group() + '/')


if __name__ == '__main__':
    main()
