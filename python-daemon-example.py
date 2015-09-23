#!/usr/bin/env python
import itertools, time

import daemon

def main():
    for i in itertools.count(1):
        time.sleep(1)
        print(i)

with daemon.DaemonContext():
    main()
