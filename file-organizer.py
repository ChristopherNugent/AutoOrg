from os import listdir, makedirs
from os.path import isfile, expanduser, join
from shutil import move
from datetime import datetime
from sys import argv
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
    if not isfile(join(dst, filename)):
        print('Moving ' + filename + ' from ' + src + ' to ' + dst)
        move(join(src, filename), join(dst, filename))
    else:
        print(join(dst, filename) + " already exists, not moving to avoid overwrite...")


def main(pattern):
    now = datetime.now()
    print(now.strftime(
        "%d-%m-%Y %H:%M:%S | Running file organizer with pattern " + pattern))
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

        move_file(f.string, src, dst)


if __name__ == '__main__':
    try:
        pattern = argv[1]
        main(pattern)
    except IndexError:
        print('Error: Pattern not specified. Exiting...')
