#!/usr/bin/env python
import sys
import os.path

if len(sys.argv) != 2:
    print "Usage: %s <file.sageews>" % sys.argv[0]
    sys.exit(1)

f = open(sys.argv[1] + ".txt", "w")

data = open(sys.argv[1]).read()
lines = [l[1:] for l in data.split(chr(0xef) + chr(0xb8))[1:] if not l.startswith(chr(0xa1))]

for l in lines:
    if l.startswith(chr(0x0a)):
        f.write("{{{\n%s\n}}}\n" % l.strip())
f.close()
