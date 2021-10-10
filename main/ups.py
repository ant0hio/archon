import subprocess
from django.shortcuts import render

args = ["apcaccess", "-f", "/etc/apcupsd/apcupsd.conf"]
#args = ["ipconfig"]


def upsresult():
    out = subprocess.check_output(args).splitlines()
    #out = "[b'APC      : 001,038,0914', b'DATE     : 2021-10-10 20:10:29 +0100  ', b'HOSTNAME : raspberrypi', b'VERSION  : 3.14.14 (31 May 2016) debian', b'UPSNAME  : raspberrypi', b'CABLE    : USB Cable', b'DRIVER   : USB UPS Driver', b'UPSMODE  : Stand Alone', b'STARTTIME: 2021-10-09 23:05:29 +0100  ', b'MODEL    : Back-UPS ES 525 ', b'STATUS   : ONLINE ', b'LINEV    : 220.0 Volts', b'LOADPCT  : 8.0 Percent', b'BCHARGE  : 100.0 Percent', b'TIMELEFT : 71.4 Minutes', b'MBATTCHG : 5 Percent', b'MINTIMEL : 3 Minutes', b'MAXTIME  : 0 Seconds', b'SENSE    : Medium', b'LOTRANS  : 195.0 Volts', b'HITRANS  : 255.0 Volts', b'ALARMDEL : 30 Seconds', b'BATTV    : 13.3 Volts', b'LASTXFER : No transfers since turnon', b'NUMXFERS : 0', b'TONBATT  : 0 Seconds', b'CUMONBATT: 0 Seconds', b'XOFFBATT : N/A', b'SELFTEST : NO', b'STATFLAG : 0x05000008', b'MANDATE  : 2006-10-03', b'SERIALNO : NB0641001496  ', b'BATTDATE : 2006-10-03', b'NOMOUTV  : 230 Volts', b'NOMINV   : 230 Volts', b'NOMBATTV : 12.0 Volts', b'NOMPOWER : 300 Watts', b'FIRMWARE : 851.t3.I USB FW:t3', b'END APC  : 2021-10-10 20:10:40 +0100  ']"
    output = out.split('b\'')
    starttime = output[9][0:-5].split(': ')
    load = output[13][0:-3].split(': ')
    charge = output[14][0:-3].split(': ')
    timeleft = output[15][0:-3].split(': ')
    ups = {
        'starttime': starttime[1],
        'load': load[1],
        'charge': charge[1],
        'timeleft': timeleft[1]
    }
    return out
