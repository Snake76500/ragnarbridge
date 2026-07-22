"""
Configuration loader
"""

from pathlib import Path
import yaml


CONFIG_FILE = Path(
    __file__
).parent / "config.yaml"


def load_config():

    with open(CONFIG_FILE, "r") as file:
        return yaml.safe_load(file)
