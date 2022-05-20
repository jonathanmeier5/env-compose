import yaml

DEFAULT_CONFIG_FILE = "env-compose.yaml"


class Config:
    def __init__(self):

        self._contents = None
        self._filepath = DEFAULT_CONFIG_FILE

    @property
    def contents(self):
        if self._contents is None:
            with open(self._filepath) as f:
                self._contents = yaml.load(f.read(), yaml.CLoader)
        return self._contents
