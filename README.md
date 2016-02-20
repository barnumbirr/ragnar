<h1><img src="https://raw.githubusercontent.com/mrsmn/ragnar/master/doc/ragnar.png" height=85 alt="ragnar" title="ragnar"> ragnar</h1>

[![PyPi Version](http://img.shields.io/pypi/v/ragnar.svg)](https://pypi.python.org/pypi/ragnar/)   [![Downloads](http://img.shields.io/pypi/dm/ragnar.svg)](https://pypi.python.org/pypi/ragnar/)

**ragnar** is an APACHE licensed Python library allowing you to decorate a function in your Python code, making it run in a separate thread.

## Installation:

From source use

		$ python setup.py install

or install from PyPi

		$ pip install ragnar

## Documentation:

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ragnar import threaded

def fib(n):
	if n < 2:
		return n
	return fib(n-2) + fib(n-1)

print fib(35)

@threaded(daemon=True)
def _fib(n):
	if n < 2:
		return n
	return fib(n-2) + fib(n-1)

print _fib(35)
```

## License:

```
	Apache v2.0 License
	Copyright 2016 Martin Simon

	 Licensed under the Apache License, Version 2.0 (the "License");
	 you may not use this file except in compliance with the License.
	 You may obtain a copy of the License at

		 http://www.apache.org/licenses/LICENSE-2.0

	 Unless required by applicable law or agreed to in writing, software
	 distributed under the License is distributed on an "AS IS" BASIS,
	 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
	 See the License for the specific language governing permissions and
	 limitations under the License.

```