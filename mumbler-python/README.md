# Learning Python

I'm learning python. This is a small coding kata I completed to practice the syntax.

## Pre-requisites
- Python:  https://www.python.org/about/gettingstarted

## Helpful Python docs:
- [unittest](https://docs.python.org/3/library/unittest.html) - the ``unittest`` module provides a rich set of tools for constructing and running tests

## Mumbling Kata

The goal of this kata is to implement the mumble_letters() method which takes a string as input and returns a formatted output string. The output string contains sequences of repeating letters with each letter repeated a number of times based on its position in the input string i.e. the 3rd letter in the string is repeated 3 times. Each sequence of repeated letters is separated with a hyphen(-) and the first letter of each sequence is capitalised.

The following examples illustrate the mumble_letters() method:

```python
mumble_letters("a")
=> "A"
```

```python
mumble_letters("abC")
=> "A-Bb-Ccc"
```

```python
mumble_letters("aBCd")
=> "A-Bb-Ccc-Dddd"
```

```python
mumble_letters("QWERTY")
=> "Q-Ww-Eee-Rrrr-Ttttt-Yyyyyy"
```

```python
mumble_letters("")
=> "" 
```

```python
mumble_letters("123")
=> Raises an exception "Sorry, no numbers allowed"
```

## Rules
Note that your ``mumble_letters()`` implementation should also handle an empty string input appropriately.

## Solution

Using TDD, implemented two files:
- [``test.py``](test.py)

Contains unit tests for the each of examples above.

- [``mumbler.py``](mumbler.py)

Contains ``mumble_letters()`` method.
