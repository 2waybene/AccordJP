import click
import sys
from . import  analysisPipeline


@click.group()
def main(args=None):
    pass

@main.command()
@click.argument('filename', type=click.Path(exists=True))
def touch(filename):
    """Print FILENAME if the file exists."""
    click.echo(click.format_filename(filename))
    analysisPipeline.launchModelStep1(filename)


@main.command()
def initdb():
    click.echo('Initialized the database')

@main.command()
def dropdb():
    click.echo('Dropped the database')

if __name__ == "__main__":
    main()
