# Playlist2Music
Playlist2Music is a tool designed to convert a single video file containing multiple music tracks into individual music files.

## How It Works
Playlist2Music parses the provided timestamp list to extract the start time for each music track. It then utilizes **FFmpeg** to split the playlist video file into individual music files based on the specified start times. Optionally, it can rename the output files to match the provided music titles.

## Requirements
1. Install [FFmpeg](https://ffmpeg.org/) on your system
2. Edit `timestamp` list in `p2m_script.py` file
    - Enter the start time for each music file in your playlist
    - **Optional**: Enter title for each music file next to the start time
3. Run p2m_script.py
    - **Optional**: Run `p2m_rename.py` to rename all output files to music title

## Example
Suppose you have a 30 minutes long video file containing 10 music tracks. By specifying the start times and optionally adding titles for each track, Playlist2Music will efficiently extract and save each track as an individual music file.

    timestamps = [
        "[00:00] Lets Be Friends",
        "[03:58] Running Over Time",
        "[07:34] Too Good At Old Town",
        "[10:45] Electric Summertime",
        "[14:10] Feel Coffee",
        "[17:54] Be with you",
        "[21:16] Too Close Driving",
        "[25:18] Kiss me Kiss me",
        "[29:07] Whispers in the Wind",
        "[32:31] Echoes of Twilight",
    ]

Output:

    output-1.mp3, output-2.mp3, output-3.mp3, ..., output-10.mp3

Optionally run `p2m_rename.py` to rename output files to music titles:

    Lets Be Friends.mp3, Running Over Time.mp3, Too Good At Old Town.mp3, ..., Echoes of Twilight.mp3
