
What is it
----

See title.
I was curious how much seeing finger moves when card owner entering pin code from credit/debit card could reduce possible pin combinations.
So here you have this shabby script.


How to use
----
./pin-hijack.py guess-pin-commands.txt

Script understand some kind of language using which you can express ideas like:
'next digit is on right of previous':
>

'it is any digit':
?

'it is digit 1 or 3 or 7'
1 3 7

'digit is on same horizontal line':
-

'digit is on same vertical line':
|

Where 'on right' (or `>`) means literally 'what is on right'.
For 1: '2 3 5 6 8 9 0'

All directions are for keypad like this:
1 2 3
4 5 6
7 8 9
  0

You can combine them.
Rules are as follow:
1. Direction commands ('<', '^', '>', ';') can be combined by two, like:
'to left and down':
<;

'to right and up':
>^

This will form INTERCEPTION.
So for '8' command '>^' narrows down to {3, 6} possibilities. Note that it does not include 2, 5 or 9.

2. Line commands ('-', '|') can be added to single direction command or combination of two.
They mean 'add horizontal/vertical line'.

So, for '8':

'>^-'
will extend to:
'3 6 8 9'

'>^|'
will extend to:
'3 6 2 5 8'

These commands work like UNION.
Also they can be used alone without any additional move commands.
Meaning 'peasant moved finger horizontally/vertically (on the same row/collumn)'.

Brief results
----

For 4-digit pin there are 10k combinations.
It is possible to reduce it to hundreds just knowing general directions. Like 'second digit is on left from first on'.
If on top of that you sure about one digit this can give you less than 100 combinations.
You can narrow it down with trained memory.


Resume
----
It was fun.
Not sure if this can have any practical benefits.
I guess resulting list of combinations can be narrowed down further with additional info (date of birthday? favorite numbers?).


Future:
----
It has no future. 
There are plenty of ways to improve 'language' so one can describe observations more throughly.
But most definitely I will not return to it.
PRs are still welcome tho.

----
Искренне ваш, Илья Легостаев, или ты Легостаев (c)КВН
