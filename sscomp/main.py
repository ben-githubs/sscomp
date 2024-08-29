#!/usr/bin/env python
""" sscomp is a command-line tool that generates a set of static web pages from a series of jinja
templates.
"""
import shutil
import pathlib
import click
import yaml
from jinja2 import Environment, FileSystemLoader, Template


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
    """Compiles Jinja templates in source_dir into static HTML pages, which are exported as files
    in dest_dir.
    """
    # -- Load Variables
    # Users can create a vars.yml (or vars.yaml) file in their src directory, which contains global
    #   variables to be referenced in their templates. We load them here.
    varfile = None
    uservars = {}
    for fname in ("vars.yml", "vars.yaml"):
        varfile = source_dir / fname
        if varfile.exists():
            break
    if varfile.exists():
        with varfile.open("r") as f:
            uservars = yaml.safe_load(f.read())

    # Create Jinja Env
    env = Environment(loader=FileSystemLoader(source_dir / "templates"), autoescape=True)

    # Generate Page Templates
    content_dir = source_dir / "content"
    templates = {}
    for item in content_dir.rglob("*"):
        # Ignore directories
        if not item.is_file():
            continue
        # Open file and load contents as string
        try:
            with item.open("r") as f:
                contents = f.read()

                # Create template page and store it
                #   We store the templates in a dictionary. The key is the "relative path" of the
                #   original template file. We'll also create the compiled HTML file at that path
                #   relative to 'dest_dir' in a later step.
                template = env.from_string(contents)
                relpath = item.relative_to(content_dir)
                templates[relpath] = template
        except UnicodeDecodeError:
            # Means this is not a text file, so we should just copy it to the dest dir
            relpath = item.relative_to(content_dir)
            templates[relpath] = item

    # Render Templates and Save Output Files
    for path, template in templates.items():
        dest_path = dest_dir / path
        # Ensure path exists
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        if isinstance(template, Template):
            rendered_page = template.render(**uservars)
            with (dest_dir / path).open("w") as f:
                f.write(rendered_page)
        elif isinstance(template, pathlib.Path):
            shutil.copy(template, dest_path)
