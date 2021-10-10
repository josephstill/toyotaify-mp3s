from pathlib  import Path
from sys      import exit
from time     import time
from argparse import ArgumentParser, BooleanOptionalAction

from toyotaify.worker.mp3 import process_mp3_track_title
from toyotaify.worker.mp3_finder import process_directory, process_single_file

if __name__ == "__main__":

    help_string = "As of 2021, the software that manages MP3 playback from Fat32 USB devices in " \
                  "Toyota vehicles doesn't sort tracks by track number when listening to an album. " \
                  "Instead the tracks are sorted alphabetically by title. This podantic application will " \
                  "prepend disk and track numbers to each MP3 so that your albums will play in order."

    parser = ArgumentParser(prog='Toyotaify', description=help_string)
    mode_group = parser.add_mutually_exclusive_group(required=True)
    mode_group.add_argument('--dir', '-d', type=Path, dest='dir',
                            help='the directory containing mp3s to process')                        
    mode_group.add_argument('--file', '-f' ,type=Path, dest='file', 
                         help='process one mp3 file')
    parser.add_argument('--recurse', action=BooleanOptionalAction, default=True,
                         help="Search through directories and subdirectories")
 
    args = parser.parse_args()
    
    worker_func = process_mp3_track_title

    if not args.dir is None:
        if not args.dir.exists() or not args.dir.is_dir():
            print(f'Error: {str(args.dir())} is not a valid directory')
            exit(2)
        start_time = time()
        stats = process_directory(args.dir, worker_func, args.recurse)
    else:
        if not args.file.exists() or args.file.is_dir():
            print(f'Error: {str(args.file)} is not a valid mp3 file')
            exit(2)
        start_time = time()
        stats = process_single_file(args.file, worker_func)

    end_time = time()
    print(f'Processing Complete:')
    print(f'Elapsed Time: {end_time - start_time} seconds')
    print(f'Files Processed: {stats[0]}')
    print(f'Directories Searched: {stats[1]}')
    print(f'Files Skipped: {stats[2]}')
    print(f'Errors: {stats[3]}') 
    exit(0)