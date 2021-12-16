import subprocess
from django.shortcuts import render

args = ["apcaccess", "-f", "/etc/apcupsd/apcupsd.conf"]
#args = ["ipconfig"]


def upsresult():
    out = subprocess.check_output(args).splitlines()
    starttime = str(out[8]).split(': ')
    load = str(out[12]).split(': ')
    charge = str(out[13]).split(': ')
    timeleft = str(out[14]).split(': ')
    ups = {
        'starttime': starttime[1][0:-3],
        'load': load[1][0:-1],
        'charge': charge[1][0:-1],
        'timeleft': timeleft[1][0:-1]
    }
    return ups
