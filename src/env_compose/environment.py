import os

from env_compose.providers import get_provider_classes

from .config import Config


def create(config: Config):

    provider_classes = get_provider_classes(config)
    env = {}
    for element in config.contents["env"]:
        provider = provider_classes[element["provider"]]
        env_element = provider.parse_element(element)
        env.update(env_element)

    return env


def update(config: Config, original_environment: dict) -> dict:
    env = create(config)
    original_environment.update(env)
    return original_environment
