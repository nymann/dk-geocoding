from pydantic import BaseModel
import requests


class Coordinates(BaseModel):
    lat: float
    lon: float


class Address(BaseModel):
    postal_code: str
    address: str
    coordinates: Coordinates


class Response(BaseModel):
    addresses: list[Address]


class Dataforsygningen:
    def __init__(self) -> None:
        self.base_url = "https://api.dataforsyningen.dk"

    def autocomplete(self, query: str) -> Response:
        response = requests.get(
            f"{self.base_url}/adresser/autocomplete",
            params={"q": query},
            timeout=3,
        )
        response.raise_for_status()
        json_response: list[dict] = response.json()
        addresses: list[Address] = []
        for entry in json_response:
            postal_code = entry["adresse"]["postnr"]
            addresses.append(
                Address(
                    postal_code=postal_code,
                    address=entry["tekst"],
                    coordinates=Coordinates(
                        lat=float(entry["adresse"]["y"]),
                        lon=float(entry["adresse"]["x"]),
                    ),
                ),
            )
        return Response(addresses=addresses)

    def reverse_geocoding(self, lat: float, lon: float) -> str:
        response = requests.get(
            f"{self.base_url}/adgangsadresser/reverse",
            params={"y": lat, "x": lon},
            timeout=3,
        )
        response.raise_for_status()
        json_response: dict = response.json()
        return json_response["adressebetegnelse"]
