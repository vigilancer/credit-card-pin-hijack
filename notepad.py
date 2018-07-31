# vim: set ts=2 sw=2 st=2 et:

'''
for pad:

    1 2 3
    4 5 6
    7 8 9
      0

'''


_left = '<'
_right = '>'
_up = '^'
_down = ';'
_self = '#'
_any = '?'
_horizontal = '-'
_vertical = '|'

COMMANDS = f'{_left}{_up}{_right}{_down}{_self}{_horizontal}{_vertical}{_any}'
ARROW_COMMANDS = f'{_left}{_up}{_right}{_down}'


def _get_hv(key, cmd):
  '''
  some heuristic to limit horizontal and vertical lines sets
  when {up, down} or {left, right} commands are in place
  because you don't need whole horizontal line when 'right' specified, right
  '''
  cats = NOTEPAD[key]
  h = set()
  v = set()

  reduced = False
  if _vertical in cmd:
    for c in {_up, _down}:
      if c in cmd:
        v = v | (cats[_vertical] & cats[c])
        reduced = True

    if reduced:
      v = v | cats[_self]
    else:
      v = cats[_vertical]

  reduced = False
  if _horizontal in cmd:
    for c in {_left, _right}:
      if c in cmd:
        h = h | (cats[_horizontal] & cats[c])
        reduced = True

    if reduced:
      h = h | cats[_self]
    else:
      h = cats[_horizontal]

  return v | h


def get_cats(key, cmd):
  cats = NOTEPAD[key]

  if _self in cmd:
    return cats[_self]

  if _any in cmd:
    return ALL

  have_arrow_command = bool(set(cmd) & set(ARROW_COMMANDS))
  if have_arrow_command:
    s = ALL
    for c in {_left, _up, _right, _down}:
      if c in cmd:
        s = s & cats[c]
  else:
    s = set()

  hv = _get_hv(key, cmd)

  return s | hv


ALL = set('0123456789')

NOTEPAD = {
  '1': {
    f'{_left}': set(''),
    f'{_up}': set(''),
    f'{_right}': set('2356890'),
    f'{_down}': set('4567890'),
    f'{_self}': set('1'),
    f'{_horizontal}': set('123'),
    f'{_vertical}': set('147'),
  },
  '2': {
    f'{_left}': set('147'),
    f'{_up}': set(''),
    f'{_right}': set('369'),
    f'{_down}': set('4567890'),
    f'{_self}': set('2'),
    f'{_horizontal}': set('123'),
    f'{_vertical}': set('2480'),
  },
  '3': {
    f'{_left}': set('1245780'),
    f'{_up}': set(''),
    f'{_right}': set(''),
    f'{_down}': set('4567890'),
    f'{_self}': set('3'),
    f'{_horizontal}': set('123'),
    f'{_vertical}': set('369'),
  },
  '4': {
    f'{_left}': set(''),
    f'{_up}': set('123'),
    f'{_right}': set('2356890'),
    f'{_down}': set('7890'),
    f'{_self}': set('4'),
    f'{_horizontal}': set('456'),
    f'{_vertical}': set('147'),
  },
  '5': {
    f'{_left}': set('147'),
    f'{_up}': set('123'),
    f'{_right}': set('369'),
    f'{_down}': set('7890'),
    f'{_self}': set('5'),
    f'{_horizontal}': set('456'),
    f'{_vertical}': set('2580'),
  },
  '6': {
    f'{_left}': set('1245780'),
    f'{_up}': set('123'),
    f'{_right}': set(''),
    f'{_down}': set('7890'),
    f'{_self}': set('6'),
    f'{_horizontal}': set('456'),
    f'{_vertical}': set('369'),
  },
  '7': {
    f'{_left}': set(''),
    f'{_up}': set('123456'),
    f'{_right}': set('2356890'),
    f'{_down}': set('0'),
    f'{_self}': set('7'),
    f'{_horizontal}': set('789'),
    f'{_vertical}': set('147'),
  },
  '8': {
    f'{_left}': set('147'),
    f'{_up}': set('123456'),
    f'{_right}': set('369'),
    f'{_down}': set('0'),
    f'{_self}': set('8'),
    f'{_horizontal}': set('789'),
    f'{_vertical}': set('2580'),
  },
  '9': {
    f'{_left}': set('1245780'),
    f'{_up}': set('123456'),
    f'{_right}': set(''),
    f'{_down}': set('0'),
    f'{_self}': set('9'),
    f'{_horizontal}': set('789'),
    f'{_vertical}': set('369'),
  },
  '0': {
    f'{_left}': set('147'),
    f'{_up}': set('123456789'),
    f'{_right}': set('369'),
    f'{_down}': set(''),
    f'{_self}': set('0'),
    f'{_horizontal}': set('0'),
    f'{_vertical}': set('2580'),
  },
}
