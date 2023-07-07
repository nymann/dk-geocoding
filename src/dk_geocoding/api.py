from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pogo_api.endpoint import Endpoint

from dk_geocoding.core.config import Config
from dk_geocoding.core.service_container import ServiceContainer
from dk_geocoding.endpoints.auto_complete import Autocomplete
from dk_geocoding.endpoints.reverse_geocoding import ReverseGeocoding


class Api:
    def __init__(self, config: Config, service_container: ServiceContainer) -> None:
        self.api = FastAPI(version=config.version, title=config.title, docs_url="/")
        self.services = service_container
        self.add_endpoints()

    @property
    def endpoints(self) -> list[Endpoint]:
        return [
            Autocomplete(dataforsygningen=self.services.dataforsygningen),
            ReverseGeocoding(dataforsygningen=self.services.dataforsygningen),
        ]

    def add_endpoints(self) -> None:
        for endpoint in self.endpoints:
            endpoint.route.add_to_router(self.api)

    def _middleware(self) -> None:
        self.api.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
