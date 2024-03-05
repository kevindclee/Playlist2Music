import subprocess
import time
from datetime import datetime

def extract_time(cur_date, timestamp):
    time_str = timestamp.split(' ')[0][1:-1]  # Extracting time part, excluding brackets
    parts = time_str.split(':')  # Splitting hours, minutes, seconds
    if len(parts) == 2:  # If only hours and minutes are given
        parts.insert(0, '0')  # Inserting 0 for hours
    h, m, s = list(map(int, parts))  # Converting parts to integers
    cur_date = cur_date.replace(hour=h, minute=m, second=s)
    cur_time = cur_date.timetuple()
    return time.strftime('%X', cur_time)

def extract_name(timestamp):
    name_str = timestamp.split(' ')[1:]  # Extracting time part, excluding brackets
    return ''.join(name_str)

def main():

    cur_date = datetime.today()

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

    time_lst = [extract_time(cur_date, ts) for ts in timestamps]
    print(time_lst)

    # ffmpeg -i sample.avi -q:a 0 -map a sample.mp3
    # ffmpeg -i sample.avi -ss 00:03:05 -to 00:03:45.0 -q:a 0 -map a sample.mp3
    command = "ffmpeg -i YourTargetVideoFile.mp4 -ss 00:00:00 -to 00:03:45.0 -q:a 0 -map a sample.mp3".split()

    index = 0
    for i in range(len(time_lst) -1):
        index = i
        starttime = time_lst[i]
        endtime = time_lst[i+1]
        command[4] = starttime
        command[6] = endtime + '.0'
        command[-1] = f'output-{i+1}.mp3'
        print(command)
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    # Last soundtrack
    # ffmpeg -i sample.avi -ss 00:03:05 -q:a 0 -map a sample.mp3
    lastcommand = "ffmpeg -i issac2.mp4 -ss 00:00:00 -q:a 0 -map a sample.mp3".split()
    starttime = time_lst[-1]
    lastcommand[4] = starttime
    lastcommand[-1] = f'output-{index+2}.mp3'
    print(lastcommand)
    result = subprocess.run(lastcommand, shell=True, capture_output=True, text=True)

if __name__ == "__main__":
    main()