import os                           # For listdir, makedirs
import os.path                      # For checking files and path joins
import shutil                       # For shutil.move
from datetime import datetime       # For logging
import re                           # For regex
import argparse


def list_files(tdir):
    """Returns files in the passed directory, ignoring folders"""
    return [f for f in os.listdir(tdir)
            if os.path.isfile(os.path.join(tdir, f))]


def filter_files(pattern, file_names):
    """Filters file names based on the passed regex and list of file names"""
    p = re.compile(pattern)
    return [p.match(f) for f in file_names if p.match(f) is not None]


def move_file(filename, src, dst, overwrite=False):
    """A file move, of filename in src to dst, creating dst if needed.
    Overwrites the file in the destination if overwrite is true"""
    os.makedirs(dst, exist_ok=True)
    if overwrite or not os.path.isfile(os.path.join(dst, filename)):
        print('Moving ' + filename + ' from ' + src + ' to ' + dst)
        shutil.move(os.path.join(src, filename), os.path.join(dst, filename))
    else:
        print(os.path.join(dst, filename) +
              " already exists, not moving to avoid overwrite...")


def main(pattern, overwrite):
    now = datetime.now()
    print(now.strftime(
        "%d-%m-%Y %H:%M:%S | Running file organizer with pattern " + pattern))
    if overwrite:
        print("Overwrite set to True")
    src = os.path.expanduser('~') + '/Documents/'
    file_names = list_files(src)
    filtered_matches = filter_files(pattern, file_names)
    if filtered_matches:
        print("Found files: {}".format(
              ', '.join([m.string for m in filtered_matches])))
    else:
        print("No matching files found.")
    for f in filtered_matches:
        dst = os.path.join(src, f.group().lower())
        move_file(f.string, src, dst, overwrite)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("pattern", help="regex to match files to move")
    parser.add_argument("-o", "--overwrite",
                        help="overwrite existing files", action="store_true")
    args = parser.parse_args()
    try:
        pattern = args.pattern
        overwrite = args.overwrite
        main(pattern, overwrite)
    except IndexError:
        print('Error: Pattern not specified. Exiting...')
