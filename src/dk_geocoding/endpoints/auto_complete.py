from pogo_api.endpoint import GetEndpoint

from dk_geocoding.domain.dataforsygningen.service import Dataforsygningen
from dk_geocoding.domain.dataforsygningen.service import Response


class Autocomplete(GetEndpoint):
    def __init__(self, dataforsygningen: Dataforsygningen) -> None:
        self.dataforsygning = dataforsygningen
        super().__init__()

    @property
    def path(self) -> str:
        return "/autocomplete"

    def endpoint(self, query: str) -> Response:
        return self.dataforsygning.autocomplete(query=query)
