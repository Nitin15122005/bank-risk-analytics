"""
Loads project configuration from YAML.
"""


import yaml

from src.constants import PROJECT_ROOT


class Config:

    def __init__(self):

        config_path = PROJECT_ROOT / "configs" / "model_config.yaml"

        with open(config_path, "r") as file:
            self.config = yaml.safe_load(file)

    @property
    def dataset(self):
        return self.config["dataset"]

    @property
    def training(self):
        return self.config["training"]

    @property
    def features(self):
        return self.config["features"]

    @property
    def models(self):
        return self.config["models"]


config = Config()