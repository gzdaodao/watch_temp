#!/usr/bin/python

from subprocess import Popen, PIPE
import sys
import time
from traceback import format_exc


AUTOFAN_TEMP = {
    'Inlet Temp': 58, 
    'Exhaust Temp': 68, 
    'Temp': 80, 
}


MINFAN_TEMP= {
    'Inlet Temp': 45, 
    'Exhaust Temp': 55, 
    'Temp': 70, 
}

class WatchTemp(object):
    def __init__(self, autofan_temp=AUTOFAN_TEMP, minfan_temp=MINFAN_TEMP, interval=3):
        self.autofan_temp = autofan_temp
        self.minfan_temp = minfan_temp
        self.interval = interval
        self.state = 'auto'

    def set_autofan(self):
        """
        设置风扇为自动调速
        """
        #开启自动转速
        cmd = 'ipmitool raw 0x30 0x30 0x01 0x01'
        p = Popen(cmd, shell=True)
        o, err=p.communicate()
        print('fan speed set to auto')
 
    def set_fanspeed(self, speed=15):
        """
        设置风扇转速
        Arg:
            speed: 百分比
        """
        #关闭自动转速
        cmd = 'ipmitool raw 0x30 0x30 0x01 0x00'
        p = Popen(cmd, shell=True)
        o, err=p.communicate()
        #设置转速
        cmd = 'ipmitool raw 0x30 0x30 0x02 0xff {}'.format(hex(speed))
        p = Popen(cmd, shell=True)
        o, err=p.communicate()
        print('fan spped set to {}%'.format(speed))
    
    def get_temps(self, keys):
        """
        获取服务器温度
        """
        cmd = 'ipmitool sdr'
        p = Popen(cmd, shell=True, stdout=PIPE)
        #o, err=p.communicate()
        o = p.stdout
        res = []
        for i in range(2000):
            try:
                r = o.readline()
                r = r.decode('utf8')
                rs = r.split('|')
                rs = [isinstance(x, str) and x.strip() or '' for x in rs]
                if not rs:
                    continue
                if rs[0] in keys:
                    rs[1] = int(rs[1].split(' ')[0].strip())
                    res.append(rs)

            except ValueError as e:
                break
            except Exception as e:
                msg = format_exc()
                print(msg)
                break
            
        return res

 
    def run(self):
        while True:
            temps = self.get_temps(self.autofan_temp.keys())
 
            if all([t[1] < self.minfan_temp.get(t[0], 0) for t in temps]) and self.state == 'auto':
                self.set_fanspeed(20)
                self.state = '20'

            for t in temps:
                if t[1] > self.autofan_temp.get(t[0], 0):
                    self.set_autofan()
                    self.state = 'auto'

           
            time.sleep(self.interval)


w = WatchTemp()
w.run()
