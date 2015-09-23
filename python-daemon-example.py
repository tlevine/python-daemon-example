#!/usr/bin/env python
import itertools, time, os

import daemon

p = os.path.abspath('counter')
def main():
    fp = open(p, 'w')
    for i in itertools.count(1):
        fp.write('%d\n' % i)
        fp.flush()
        time.sleep(1)

with daemon.DaemonContext():
    main()
