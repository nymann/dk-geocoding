from dk_geocoding.core.config import Config
from dk_geocoding.domain.dataforsygningen.service import Dataforsygningen


class ServiceContainer:
    def __init__(self, config: Config) -> None:
        self.config = config
        self.dataforsygningen = Dataforsygningen()
