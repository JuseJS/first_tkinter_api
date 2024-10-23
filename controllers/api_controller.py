import requests
from models.api_response import APIResponse
from dataclass_wizard import fromdict


class APIController:
    _api_data = None

    @classmethod
    def fetch_api_data(cls):
        if cls._api_data is None:
            response = requests.get('https://dummyjson.com/products')
            if response.status_code == 200:
                data = response.json()
                cls._api_data = fromdict(APIResponse, data)
            else:
                cls._api_data = None
        return cls._api_data