#!/usr/bin/env python
# vim: set ts=2 sw=2 st=2 et:

import argparse
from pathlib import Path

from notepad import COMMANDS, ALL, get_cats

'''
Commands:
  < - left
  > - right
  ^ - up
  ; - down
  # - same
  ? - any
  space separated digits (ex.: '1 2 3 7 0')

File format:
  1: 1st digit variants
  2: where is 2nd digit
  3: where is 3rd digit
  4: where is 4th digit

Possible improvements:
  File format:
    5: digits that are definitely in pin (in any order, space separated)
    6: digits that are on specific places in pin (ex.: '? 3 ? 5')
  Commands:
    ? - don't know

'''


def _find_cats(prev_cat, cmd):
    try:
      int(cmd[0])
      return set(cmd.split())
    except ValueError:
      return get_cats(prev_cat, cmd)


def process(file):
  with open(file, 'r') as f:
    cmds = [next(f).strip() for x in range(4)]

  for n1 in _find_cats(None, cmds[0]):
    for n2 in _find_cats(n1, cmds[1]):
      for n3 in _find_cats(n2, cmds[2]):
        for n4 in _find_cats(n3, cmds[3]):
          print('%s%s%s%s' % (n1, n2, n3, n4))


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('file', type=Path, nargs=1)
  args = parser.parse_args()

  process(args.file[0])


if __name__ == '__main__':
  main()
