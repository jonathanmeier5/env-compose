import os
import shlex

import click
import sh

from env_compose import environment
from env_compose.config import Config


def parse_command(command: str):
    parsed_command = shlex.split(command)
    sh_command = sh.Command(parsed_command[0])
    sh_command = sh_command.bake(parsed_command[1:])
    return sh_command


@click.group()
def cli():
    """CLI for env_compose package"""
    pass


@cli.command()
@click.option("--command", "-c", multiple=False, help="Command to run.")
def run(command):
    new_env = os.environ.copy()
    env = environment.update(Config(), new_env)
    run_command = parse_command(command)
    run_command(_fg=True, _env=env)
    click.echo(f"Execute {command}")


@cli.command()
def view():
    env = environment.create(Config())
    click.echo(env)
