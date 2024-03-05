import subprocess
import time
from datetime import datetime

def extract_name(timestamp):
    name_str = timestamp.split(' ')[1:]  # Extracting time part, excluding brackets
    return ''.join(name_str)

def main():

    timestamps = [
        "[00:00] Lets Be Friends",
        "[03:58] 나쁘지 않아",
        "[07:34] 지친하루",
        "[10:45] 봄아",
        "[14:10] 오늘도 꿈에서 그대가",
        "[17:54] Be with you",
        "[21:16] 그 밤을 내게 줘요",
        "[25:18] Kiss me Kiss me",
        "[29:07] 나를 쏘다",
        "[32:31] 내 기억속의 소년",
        "[37:05] Dive in",
        "[41:02] 별 같아서",
        "[44:50] 잠",
        "[48:10] 소년",
        "[52:12] 숲",
        "[55:09] 모닥불",
        "[59:49] 비",
        "[1:02:34] 기다림",
        "[1:05:50] 휘",
        "[1:10:03] 지금은 아무것도 몰라도",
        "[1:13:18] 마음이 내려 쌓이면",
        "[1:16:55] 너와 함께",
        "[1:22:11] I Love You",
        "[1:25:27] 잠자리 지우개",
        "[1:30:17] 바다야 안녕",
        "[1:34:06] 네가 없는 하루"
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