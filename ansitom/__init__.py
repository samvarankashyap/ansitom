import os
import click

class Context(object):
    """ Global Context object accesible by all the click modules """
    def __init__(self):
        self.clipath = os.path.dirname(os.path.realpath(__file__))
        self.version = "0.0.2"

pass_context = click.make_pass_decorator(Context, ensure=True)

@click.group()
@click.option('--verbose', is_flag=True)
@pass_context
def cli(context, verbose):
    """
    Welcome to Ansitome command line
    """
    click.echo("Version: "+context.version)
    click.echo("Ansitom Ansitom Ansitom")
    print "hello"

@cli.command()
@pass_context
def init(config):
    """ init module of ansitom """
    click.echo('Initailise Ansitom :P !')
