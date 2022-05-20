import os
import shlex

import click
import sh

from env_compose import environment
from env_compose.config import Config


def parse_command(command: tuple):
    sh_command = sh.Command(command[0])
    sh_command = sh_command.bake(command[1:])
    return sh_command


@click.group()
def cli():
    """CLI for env_compose package"""
    pass


@cli.command()
@click.argument("args", nargs=-1)
def run(args):
    click.echo(f"Execute {args}")
    new_env = os.environ.copy()
    env = environment.update(Config(), new_env)
    run_command = parse_command(args)
    run_command(_fg=True, _env=env)


@cli.command()
def view():
    env = environment.create(Config())
    click.echo(env)
