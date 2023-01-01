# Python tutorial

[tutorial link](https://naucse.python.cz/course/pyladies/beginners/venv-setup/)

All commands are for windows cmd...

## Setup
Create venv:  
`py -3 -m venv venv`

Install deps:  
`venv\Scripts\activate`  
`python -m pip install -r requirements.txt`

## Run
First activate venv:  
`venv\Scripts\activate`

Then start any `py` file:  
`cls & python base/01_henlo.py`

`base/04_cycles.py` can be just opened from explorer...

Deactivate venv:  
`deactivate`

## Development

Save deps:  
`python -m pip freeze > requirements.txt`

Run tests:  
`python -m pytest -v base/09_testable.py`

Lol :)
