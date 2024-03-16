import sys

from waitress import serve
from src.api import app

if __name__ == "__main__":
    print('HENLO')
    serve(app, host='localhost', port=8080)
