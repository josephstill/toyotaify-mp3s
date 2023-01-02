# Toyotaify-MP3s
If you've tried to play music from a USB storage device in a Toyota, then you were likely frustrated when trying to listen to an album from start to finish. This is because the head unit sorts tracks alphabetically by name instead of using the track number which is encoded into the MP3. When faced with streaming services, [which are bad for artists](https://www.nytimes.com/2021/05/07/arts/music/streaming-music-payments.html), or buying an ipod, I chose to stick with my microSD cad and USB adapter. This tool helps me edit MP3 tags in mass.  
  
## Usage
The tool is simple to run and need not be installed. From the root directory of the project do this:  
  
```
python -m toyotaify -d </path/to/mp3/files> 
```

This will recurese through the directory tree specified and update all MP3s that have a valid track number field.  
