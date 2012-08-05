#!/usr/bin/env python
# encoding: UTF-8

import os
import sys
import re

for line in sys.stdin:
    match = re.match(r'^(.*?): yes$', line)
    if match:
        sys.stdout.write(match.group(1) + ": true\n")
        continue
    match = re.match(r'^(.*?): no$', line)
    if match:
        sys.stdout.write(match.group(1) + ": false\n")
        continue
    if re.match(r'^.*?:$', line.rstrip()):
        sys.stdout.write(line.rstrip() + " \n")
    else:
        sys.stdout.write(line)

      