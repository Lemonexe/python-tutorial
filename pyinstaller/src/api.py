from flask import Flask
# just try removing numpy, and return just "OK" from the is_it_up
# you'll see that dist\serve.exe will get considerably smaller
# which proves that pyinstaller includes only actually imported libs, not all libs from virtualenv
import numpy as np

app = Flask(__name__)


@app.get('/hello')
def is_it_up():
    """Return OK to check if the server is up."""
    a = np.array([1,2,3,4])
    return f'{np.mean(a)}'

@app.get('/e')
def eee():
    """Return OK to check if the server is up."""
    return {'error': "The entity was not very processable"}, 422
