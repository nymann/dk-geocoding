from pogo_api.endpoint import GetEndpoint
from pydantic import BaseModel


class Response(BaseModel):
    lat: float
    lon: float


class Geocoding(GetEndpoint):
    def endpoint(self, address: str, postal_code: str) -> Response:
        return Response(lat=56.0387294, lon=9.9599287)
