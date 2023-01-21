# Python tutorial

[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/PyCQA/pylint)
_Lol JK not rly.._

[tutorial base](https://naucse.python.cz/course/pyladies/)  
[tutorial MI-pyt](https://naucse.python.cz/course/mi-pyt/)

All commands are for windows cmd...


## Setup

### Install
Install [python](https://www.python.org/downloads/), [follow guide](https://naucse.python.cz/course/pyladies/beginners/install/windows/)  
Then `pip install --user pipenv`  
Add to path, typically at `%userprofile%\AppData\Roaming\Python\Python311\Scripts`

### vanilla setup
Create venv:  
`py -3 -m venv venv`

Install deps:  
`venv\scripts\activate`  
`python -m pip install -r requirements.txt`

### pipenv setup
Create venv, install deps:  
`pipenv install`

## Run

### vanilla

First activate venv: `venv\scripts\activate`  
(deactivate: `deactivate`)

Then start any `py` file:  
`cls & python base/01_henlo.py`

Btw only the file `base/04_cycles.py` can simply be opened from explorer...


### pipenv

Either activate shell: `pipenv shell`  
(deactivate: `exit`)

Or run files through pipenv run **(preferred)**:  
`cls & pipenv run python base/01_henlo.py`


## Development

Install a new dep: `pipenv install numpy`

Save deps after any install – for vanilla pip:  
`python -m pip freeze > requirements.txt`

Run tests:  
`test.bat`

Run Prettier:  
`pipenv run prettier`

Lint kind of? Not really using it..  
`pipenv run lint`

Lol :)
