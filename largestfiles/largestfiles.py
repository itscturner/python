#!/usr/bin/python

import os
import sys

size = 0
max_size = 0
max_file = ""

if len(sys.argv) > 1:
  path = sys.argv[1]
else:
  print("No directory was provided. Exiting.")
  print()
  os._exit(1)

for folder, subfolders, files in os.walk(path):

  for file in files:
    size = os.stat(os.path.join(folder, file)).st_size

    if size>max_size:
      max_size = size
      max_file = os.path.join(folder, file)

print("The largest file size is: " + max_file)
print('Size: ' + str(max_size) + ' bytes')
