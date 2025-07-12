"""
Ensures a config.yml FILE exists, if its a empty folder, remove it and put in the example template
"""

from pathlib import Path


def main():
    root = Path(__file__).parent.parent
    config_path = root / "config.yml"
    config_example = root / "config.example.yml"

    if not config_path.exists():
        config_path.write_text(config_example.read_text())
        quit()

    if config_path.is_dir():
        config_path.rmdir()
        config_path.write_text(config_example.read_text())
        quit()


if __name__ == "__main__":
    main()
