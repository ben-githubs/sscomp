"""
sscomp is a command-line tool that generates a set of static web pages from a series of jinja
templates.
"""

import pathlib
import click

import sscomp.core


@click.command()
@click.argument(
    "source_dir",
    type=click.Path(
        exists=True, file_okay=False, readable=True, resolve_path=True, path_type=pathlib.Path
    ),
)
@click.argument(
    "dest_dir",
    type=click.Path(
        exists=True, file_okay=False, writable=True, resolve_path=True, path_type=pathlib.Path
    ),
)
def compile_website(source_dir: pathlib.Path, dest_dir: pathlib.Path):
    """Compiles the site in 'source_dir' and exports the result to 'dest_dir'."""
    return sscomp.core.compile_website(source_dir, dest_dir)
