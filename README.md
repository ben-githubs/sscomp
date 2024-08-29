# sscomp: Static Site Compiler

sscomp is a small CLI tool designed to compile several Jinja templates into a static website. Inspired by Flask, the tool aims to make it easy to reuse HTML constructs and templates for simple websites that don't require a full backend server.

## Installation

From inside the repo, run

```bash
pip install dist/sscomp-{version}-py3-none-any.whl
```

Replace `{version}` with the desired version for installation.

## Usage

The tool requires a source directory, `src`, which contains your templates, configuration files, and website structure. For example:

- src
  - content
    - index.html
    - about.html
    - contact.html
  - templates
    - main.jinja2
    - navbar.jinja2
    - index.jinja2
  - vars.yml

Then, the process of compiling the site is simple:

```bash
sscomp src_dir dest_dir
```

where `src_dir` is the location of your content and templates (`src\` in the example above), and `dest_dir` is where you'd like the static HTML pages to be placed (for example, `mysite\`).

### Vars File

The vars file makes it easy to specify some global configuration values you can reference in your templates. The file must be called `vars.yml` or `vars.yaml`. Any values set therein can be referenced in your jinja templates by name.

For example, if your `vars.yml` file has

```yaml
title: My Cool Website
```

then in your jinja templates, you could say

```html
<head>
    <title>{{ title }}</title>
</head>
```

Vars can be nested to emulate namespaces, if desired:

```yaml
stylesheets:
  main: 'static/main.css'
  contact: 'static/contact.css'
```

```html
<head>
    <link rel="stylesheet" href="{{ stylesheets.main }}">
    <link rel="stylesheet" href="{{ stylesheets.contact }}">
</head>
```