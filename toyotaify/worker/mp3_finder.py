from pathlib import Path
from typing  import Callable

def process_directory(directory: Path, worker: Callable[[Path], tuple], recurse: bool = True) -> tuple:
    files = 0
    dirs = 1
    skips = 0
    errors = 0
    for child in directory.iterdir():
        if child.suffix == '.mp3':
            ret = worker(child)
            files += ret[0]
            errors += ret[1]
        elif child.is_dir() and recurse:
           print(f'Processing files in {str(child)}')
           ret = process_directory(child, worker, recurse) 
           files += ret[0]
           dirs += ret[1]
           skips += ret[2]
           errors += ret[3]
        else:
            skips += 1
    return files, dirs, skips, errors

def process_single_file(mp3: Path, worker: Callable[[Path], tuple]) -> tuple:
    files = 0
    skips = 0
    errors = 0
    if mp3.suffix == '.mp3':
        print(f'Processing {str(mp3)}')
        ret = worker(mp3)
        files += ret[0]
        errors += ret[1]
    else:
        skips = 1
    return files, 0, skips, errors 