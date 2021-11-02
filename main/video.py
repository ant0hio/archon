import subprocess
from django.shortcuts import render

args = ["ffmpeg", "-rtsp_transport tcp", "-i \"rtsp://user:user@192.168.100.22:554/profile0\"","-c copy", "-an", "-movflags", "+frag_keyframe+separate_moof+omit_tfhd_offset+empty_moov", "/home/pi/PyProjects/archon/archon/media/video.mp4"]


def ffmpeg_start():
    out = subprocess.check_output(args)
    return out

