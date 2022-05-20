import abc
import functools

from env_compose.config import Config


class Provider(abc.ABC):
    def __init__(self, config: Config = None):
        self.config = config

    @abc.abstractmethod
    def parse_element(self, element):
        raise NotImplemented()


class StaticProvider(Provider):
    def parse_element(self, element):
        env_element = {element["key"]: element["value"]}
        return env_element


class FileProvider(Provider):
    def parse_element(self, element):

        filename = element["filename"]
        env_element = {}
        with open(filename, "r") as f:
            for line in f.readlines():
                k, v = line.split("=")
                v = v.rstrip("\n")
                env_element[k] = v
        return env_element


@functools.lru_cache()
def get_provider_classes(config):

    classes = {
        "static": StaticProvider(config=config),
        "file": FileProvider(config=config),
    }

    return classes
