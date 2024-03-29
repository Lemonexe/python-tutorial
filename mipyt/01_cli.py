# python mipyt/01_cli.py --count 4 --name "Jiri"

# click library helps to create interactive CLI applications (which is ofc possible w/o it)
import click
import os

# it uses DECORATORS
@click.command() # this causes click to process the sys.argv
@click.option('-c', '--count', default=1,  metavar='COUNT', help='Number of greetings.') # has default value
@click.option('-n', '--name', prompt='Your name', metavar='NAME', help='The person to greet.') # has prompt as default
@click.option('-v', '--verbose', is_flag=True, help='More verbose output') # is boolean, no value
# they respond either to -c or --count, as per unix convention

# the first three args are injected from the decorators
def hello(count, name, verbose):
    dir = os.getcwd()
    for x in range(count):
        click.echo(f"Hello {name}, we are in directory {dir}")
    if verbose:
        click.echo('Nice to meet you')

def another_fn(count, name, verbose):
    print(count, name)
# another_fn() # this errors out because this function is not decorated

# if the file is executed directly, else if imported, the sys.argv wouldn't be available
if __name__ == '__main__':
    hello()

# btw click can also be used for arguments or file opening etc.
# arguments are like options but obligatory & with given order, not identified the --name
