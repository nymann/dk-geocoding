from pogo_api.endpoint import GetEndpoint
from pydantic import BaseModel


class Coordinates(BaseModel):
    lat: float
    lon: float


class Address(BaseModel):
    postal_code: str
    address: str
    coordinates: Coordinates


class Response(BaseModel):
    addresses: list[Address]


class AutoComplete(GetEndpoint):
    @property
    def path(self) -> str:
        return "/auto-complete"

    def endpoint(self, query: str) -> Response:
        return Response(
            addresses=[
                Address(
                    postal_code="8660",
                    address="Harevej 13, 8660 Skanderborg",
                    coordinates=Coordinates(lat=56.0387294, lon=9.9599287),
                ),
            ],
        )
