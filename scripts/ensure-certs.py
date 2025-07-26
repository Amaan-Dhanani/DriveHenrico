"""
Ensures cert files for development are generated
"""

import sys
sys.dont_write_bytecode = True

import os
import subprocess
from typing import Literal

import yaml
import shutil
import platform
from pathlib import Path


def has_cmd(name: str) -> bool:
    return True if shutil.which(name) is not None else False

def run(command: str, cwd: Path):
    subprocess.run(command.split(" "), cwd=cwd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Universal
HAS_MKCERT = has_cmd("mkcert")

# Arch
HAS_PACMAN = has_cmd("pacman")

# Windows
HAS_CHOCO = has_cmd("choco")
HAS_SCOOP = has_cmd("scoop")

OS: Literal["Linux", "Windows"] = platform.system()
if OS not in ["Linux", "Windows"]:
    raise OSError("Not linux or windows operating system")

if not HAS_MKCERT:
    raise OSError("This script requires `mkcert` to be installed")

root: Path = Path(__file__).parent.parent
config: dict = yaml.load((root / 'config.yml').read_text(), Loader=yaml.FullLoader)
app_domain: str = config["app_domain"]
call_folder = Path(os.getcwd())

# Check if certs dir exists
certs_folder = root / "certs"
if not certs_folder.exists():
    certs_folder.mkdir()

expected_certs = [app_domain, f"api.{app_domain}"]

# Delete current files
for file in certs_folder.glob("*.pem"):
    file.unlink()

run("mkcert -install", certs_folder)
for cert in expected_certs:
    run(f"mkcert {cert}", certs_folder)
