# Airbnb Clone

### Description
This repository contains code to create a console for the AirBnB clone. The console gives users access to a command line interpreter to manipulate classes and objects in the clone website


### Some available commands
1. `create` creates a new instance of a class. ex `create <class>`

2. `update` updates object attributes. ex `update <class> <object_id> <attribute name> <value>`

3. `destroy` destroys an object with given id. ex `<destroy> <class> <object_id>` or `<class>.<destroy>(id)`

4. `show` displays an object with specific class and id. ex `<class>.<show>(id)`

5. `count` displays the number of objects of a given class. ex `<class>.<count>()`


## Installation

```
git clone https://github.com/Verlyndy1/AirBnB_clone.git
cd AirBnB_clone
```

## Usage
### Interactive mode

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

### Non interactive mode
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```


### Environment
Language: Python3,
Tested on Ubuntu 20.04 LTS,
Style guidelines PEP 8 (version 1.7) || Google Style Python Docstrings

# AUTHORS
#### Caleb Adinfono, Marylynda Oluchukwu Ezenwanne
