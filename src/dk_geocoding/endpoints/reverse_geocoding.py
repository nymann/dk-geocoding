from pogo_api.endpoint import GetEndpoint

from dk_geocoding.domain.dataforsygningen.service import Dataforsygningen


class ReverseGeocoding(GetEndpoint):
    def __init__(self, dataforsygningen: Dataforsygningen) -> None:
        self.dataforsygning = dataforsygningen
        super().__init__()

    @property
    def path(self) -> str:
        return "/reverse-geocoding"

    def endpoint(self, lat: float, lon: float) -> str:
        return self.dataforsygning.reverse_geocoding(lat=lat, lon=lon)
