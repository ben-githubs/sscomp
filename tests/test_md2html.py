"""Tests that md2html works."""

from io import StringIO
from pathlib import Path
import shutil

from lxml import etree

from sscomp.core import compile_website

FIXTURE_PATH = Path(__file__).parent / "fixtures/md2html"

def test_md2html(tmp_path):
    src = FIXTURE_PATH / "src"
    dst = tmp_path / "dst"

    # Delete dst if it alreadyt exists
    if dst.exists():
        shutil.rmtree(dst)
    dst.mkdir()

    compile_website(src, dst)

    dst_file = (dst / "index.html")
    assert dst_file.exists()

    # Check if HTML is valid
    parser = etree.HTMLParser(recover=False)
    with dst_file.open("r") as f:
        etree.parse(f, parser)