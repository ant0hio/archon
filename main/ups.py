import subprocess
from django.shortcuts import render

args = ["apcaccess", "-f", "/etc/apcupsd/apcupsd.conf"]
#args = ["ipconfig"]

def upsresult():
    out = subprocess.check_output(args).splitlines()
    return out

