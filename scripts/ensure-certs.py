"""
Ensures cert files for development are generated
"""

import os
import sys
from typing import Literal
sys.dont_write_bytecode = True

import platform
import yaml
import shutil
from pathlib import Path


def has_cmd(name: str) -> bool:
    return True if shutil.which(name) is not None else False

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
    match OS:
        case "Linux":
            if not HAS_PACMAN:
                raise OSError("Pacman not found, required for this command")
            
            os.system("sudo pacman -S mkcert")
            
            
        case "Windows":
            if True not in [HAS_CHOCO, HAS_SCOOP]:
                raise OSError("Requires either choco or scoop to install")
            
            if HAS_CHOCO:
                os.system("choco install mkcert")
            
            if HAS_SCOOP:
                os.system("scoop install mkcert")

root: Path = Path(__file__).parent.parent
config: dict = yaml.load((root / 'config.yml').read_text(), Loader=yaml.FullLoader)
app_domain: str = config["app_domain"]
call_folder = Path(os.getcwd())

# Check if certs dir exists
certs_folder = root / "certs"
if not certs_folder.exists():
    certs_folder.mkdir()
    
expected_certs = [app_domain, f"api.{app_domain}"]

# Go to certs dir


os.chdir(certs_folder)
os.system("mkcert -install")

for cert in expected_certs:
    os.system(f"mkcert {cert}")
    
os.chdir(call_folder.resolve())




