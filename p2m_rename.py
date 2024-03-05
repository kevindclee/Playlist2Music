import subprocess
import time
from datetime import datetime

def extract_name(timestamp):
    name_str = timestamp.split(' ')[1:]  # Extracting time part, excluding brackets
    return ''.join(name_str)

def main():

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

    name_lst = [extract_name(ts) for ts in timestamps]

    # ffmpeg -i sample.avi -q:a 0 -map a sample.mp3
    # ffmpeg -i sample.avi -ss 00:03:05 -to 00:03:45.0 -q:a 0 -map a sample.mp3
    command = "ren input.txt output.txt".split()

    index = 0
    for i in range(len(name_lst)):
        command[1] = f'output-{i+1}.mp3'
        command[2] = f'Musician-{name_lst[i]}.mp3'
        print(command)
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

if __name__ == "__main__":
    main()