from pyrootutils import setup_root
from os import getcwd

ROOT = setup_root(getcwd(), dotenv=True, pythonpath=True, cwd=True)