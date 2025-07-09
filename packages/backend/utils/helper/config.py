"""
This module has one simple purpose: Find and Parse given configuration files.
In this file, imports are handled
"""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Optional

import yaml

from siblink import Config

_BLANK = object()

class Primitive(ABC):
    """
    Primitive config loader and parser helper class
    
    Interfaces
    ----------
    `parse()
    > test
    """
    
    @Config.load_predetermined
    def __init__(self, path: Optional[str] = None, lazy: bool = False, default: str = ""):
        """
        Before anything, makes sure that the config is fully loaded and ready to go.
        This includes root folders, os env specs etc.


        Properties
        ----------
        file: Optional[Path]
            Path object to the file in question, only accessible if the file exists


        :param str file: Name of the file that will be used        
        :param bool lazy: Whether or not to create the file if it doesn't exist
        :param str default: If lazy is specified, this is what is written to the file to create it
        :raises FileNotFoundError: Whenever no `path` is supplied or the "discovered" file doesn't exist       

        """

        self.file: Optional[Path] = None

        # Make sure a path is given
        if path is None:
            raise FileNotFoundError("No path specified")

        _project_root: Path = Config.root
        _config_file: Path = _project_root / path

        while not _config_file.exists():

            if not lazy:
                raise FileNotFoundError(f"Config File Not Found: {_config_file.resolve()}")

            _config_file.write_text("", encoding="utf-8")

            break

        self.file = _config_file
        
    def read(self, lazy: bool = False, default: str = ""):
        """
        Reads the specified file given to the __init__ function
        
        :param bool lazy: If this is true, the file is created if it doesn't exist
        :param str default: If lazy is specified and the file is created, this is what will be written into it.
        
        :raises FileNotFoundError: If no file was handled or the file doesn't exist and lazy isn't specified
        """
        
        # Checks if the file was even handled
        if self.file is None:
            raise FileNotFoundError("File not loaded, and or doesn't exist")
        
        while not self.file.exists():
            
            if not lazy:
                raise FileNotFoundError(f"Config File Not Found: {self.file.resolve()}")
            
            self.file.write_text(default)
            
            break
        
        return self.file.read_text(encoding="utf-8")
    
    @abstractmethod
    def parse(self, lazy: bool = False, default: Optional[Any] = _BLANK) -> dict:
        """
        Parses the given file, returns a dictionary object.
        
        :param bool lazy: Whether to create the file if it doesn't exist
        :param Optional[Any] default: Object that is returned if parsing fails        
        :returns dict: Dict representation of configuration
        """
        pass
            


class Yaml(Primitive):
    """Yaml Config Loader

    Attempts to locate and parse a .yaml file
    """

    def __init__(self, path: str = "config.yaml"):
        super().__init__(path)
        
    def parse(self, lazy: bool = False, default: Optional[Any] = _BLANK) -> dict:
        contents: str = self.read(lazy, "")
        return yaml.load(contents, Loader=yaml.FullLoader)
