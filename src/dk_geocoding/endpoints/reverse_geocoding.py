from pogo_api.endpoint import GetEndpoint


class ReverseGeocoding(GetEndpoint):
    @property
    def path(self) -> str:
        return "/reverse-geocoding"

    def endpoint(self, lat: float, lon: float) -> str:
        return "Harevej 13, 8660 Skanderborg"
