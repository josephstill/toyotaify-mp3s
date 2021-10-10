from mutagen.easyid3 import EasyID3
from pathlib         import Path

def process_mp3_track_title(mp3_file: Path) -> tuple:
    files = 0
    errors = 0
    try:
        tag = EasyID3(str(mp3_file))
        track_number = tag['tracknumber'][0]
        disk_number = ''
        if 'discnumber' in tag:
            disk_number = tag['discnumber'][0]
            if '/' in disk_number:                
                disk_num_data = disk_number.split('/')
                disk_number = disk_num_data[0].zfill(2)
            else:
                disk_number = disk_number.zfill(2)
        if "/" in track_number:
            track_number = track_number.split('/')[0]
        new_title_tag = f"{disk_number}{track_number.zfill(2)} - {tag['title'][0]}"
        tag["title"] = new_title_tag
        tag.save()
        files = 1
    except:
        print(f'Error: Parse issue with {str(mp3_file)}, skipping')
        errors = 1
    return (files, errors)