#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

def get_special_paths(dir):
  filenames = os.listdir(dir)
  result = []
  for fname in filenames:
    match = re.search(r'__(\w+)__', fname)
    if match:
      result.append(os.path.abspath((os.path.join(dir, fname))))
  return result

def copy_to(paths, dir):
  for path in paths:
    shutil.copy(path, os.path.abspath(dir))
  return

def zip_to(paths, zipPath, zipName):
  cmd = 'zip -j ' + zipName
  for path in paths:
    cmd += ' ' + path
  os.system(cmd)
  return

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  isTodir = False
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]
    isTodir = True
  
  isTozip = False
  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]
    isTozip = True

  if len(args) == 0:
    print("error: must specify one or more dirs")
    sys.exit(1)

  # +++your code here+++
  # Call your functions

  dir = args[1]
  specialPaths = get_special_paths(dir)
  if isTodir == False and isTozip == False:
    for path in specialPaths:
      print(path)
  if isTodir:
    copy_to(specialPaths, os.path.abspath(todir))
  if isTozip:
    zip_to(specialPaths, specialPaths, tozip)
    
  
if __name__ == "__main__":
  main()
