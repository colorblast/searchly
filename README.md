# searchly
duckduckgo instant answers in the terminal

## To install

Git clone and optionally make a virtualenv for it if you like. <br><pre>$ pip install json requests<br>$ chmod +x searchly <br>$ ./searchly</pre>.

## Features

All of the following is as far as I can tell
* Supports all English definitions
* Supports all entities
* Is small and only relies on requests and json

## Bugs and Limitations

* does not support languages other than English
* for some queries like bob, it will produce Microsoft BobA Microsoft product... neglecting the space
* for some queries it will not get the general search result
* it sources almost all of it from only wikipedia
