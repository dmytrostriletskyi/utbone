# utbone

Make templates for faster unit testing.

[![Travis](https://travis-ci.org/dmytrostriletskyi/utbone.svg?branch=develop)](https://travis-ci.org/dmytrostriletskyi/utbone)
[![Release](https://img.shields.io/github/release/dmytrostriletskyi/utbone.svg)](https://github.com/dmytrostriletskyi/utbone/releases)
![Python3](https://img.shields.io/badge/Python-2.7-brightgreen.svg)
![Python3](https://img.shields.io/badge/Python-3.5-brightgreen.svg)
![Python3](https://img.shields.io/badge/Python-3.6-brightgreen.svg)


## Bones for

- `unittesting`.
- `unittesting` already with `mock` and `ddt`.
- django testing.
- django testing already with `mock` and `ddt`.

## Install

Following command in your terminal:

```
pip install utbone
```

Or install source code and follow this:

```
python setup.py install
```

## Quick start or how to use

For creating [this](https://github.com/dmytrostriletskyi/utbone/blob/develop/utbone/bones/django-toppings.py) bone
with name `test_views` in `mysite/polls/tests` use next command:

```
utbone mysite/polls/tests test_views django --topping
```

`--topping` here means, that you need ready `mock` and `ddt`.

Result is next:

```python
"""
Tests for
"""
from ddt import ddt, data, unpack
from mock import patch

from django.test import TestCase


class Test(TestCase):
    """
    Tests for
    """

    def setUp(self):
        """
        Initialize
        """
        pass

    def test_first(self):
        """
        Verify that
        """
        self.assertEqual(1, '1')

    @patch('')
    def test_second(self, mock_):
        """
        Assert that
        """
        pass

    @data(
        ('first', 'second', 'expected'),
        ('first', 'second', 'expected'),
    )
    @unpack
    def test_third(self, first, second, expected):
        """
        Make sure when
        """
        pass
```


## CLI

`utbone` is easy to understand: utbone [path to append bone] [name for test] [type of test] -[t]/--[topping].
`-t` or `--topping` (the same option) is an optional parameter.

Follow this command to call full guide how to use this tool:

```
utbone --help
```
