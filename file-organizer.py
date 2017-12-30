from os import listdir, makedirs
from os.path import isfile, expanduser, join
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
    move(join(src, filename), join(dst, filename))


def main(pattern):
    now = datetime.now()
    print(now.strftime("%d-%m-%Y %H:%M:%S | Running file organizer..."))
    src = expanduser('~') + '/Documents/'
    file_names = list_files(src)
    filtered_matches = filter_files(pattern, file_names)
    if filtered_matches:
        print("Found files: " +
              ', '.join([m.string for m in filtered_matches]))
    else:
        print("No matching files found.")
    for f in filtered_matches:
        dst = join(src, f.group().lower())
        print(
            'Moving ' +
            f.string +
            ' from ' +
            src +
            ' to ' + dst)
        move_file(f.string, src, dst)


if __name__ == '__main__':
    main('^\w{3}\d{3}')
