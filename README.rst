=======
Todo.py
=======

Todo.py is a dead easy todo list runs on your command line lets you simply get things done. 

Install
-------

.. code-block::

    $ pip install todo.py

Usage
-----

Show help

.. code-block::

    $ todo --help
    usage: todo [-h] [-v] {add,delete,update,list,reset} ...

    positional arguments:
        {add,delete,update,list,reset}

    optional arguments:
        -h, --help            show this help message and exit
        -v, --version         show program's version number and exit

Add todos

.. code-block::

    $ todo add 'Hello World!'
    $ todo add 'Howdy you?'

List todos

.. code-block::

    $ todo list
    0 'Hello World!'
    1 'Howdy you?'

Update todos

.. code-block::

    $ todo update 1 'How are you doing today?'
    $ todo list
    0 'Hello World!'
    1 'How are you doing today?'

Delete todos

.. code-block::

    $ todo delete 0
    $ todo list
    0 'How are you doing today?'

Reset todos

.. code-block::

    $ todo reset
    $ todo list
    ...

Enjoy!

License
-------
Copyright (c) 2012 Kadir Pekel.

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the 'Software'), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
