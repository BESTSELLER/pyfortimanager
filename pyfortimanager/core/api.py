import requests
from dataclasses import field
from typing import Generic, List, Optional, TypeVar, Union
from pydantic import BaseModel as PBaseModel


class FMGObject(PBaseModel):
    pass


T = TypeVar("FMGObject")
class FMGResponse(Generic[T]):
    """Response to a request

    Attributes:
        data (dict|List[FMGObject]): response data
        status (int): status code
        success (bool): True on success
        message (optional[str]): error message if an error occured, else None
    """

    data: Union[dict, List[T]] = field(default_factory=dict)  # data from FMG
    status: int = 0  # status code of the request
    success: bool = False  # True on successful request
    message: Optional[str] = None # error message if an error was found

    def __bool__(self) -> bool:
        return self.success

    def first(self) -> Optional[Union[T, dict]]:
        """Return first data or None if result is empty"""
        if isinstance(self.data, dict):
            if isinstance(self.data.get("data"), list):
                return self.data.get("data")[0] if self.data.get("data") else None
            else:
                return self.data
        elif isinstance(self.data, list) and self.data:  # non-empty list
            return self.data[0]
        
        return None
    

class BaseModel:
    """API class for FortiManager login management and post requests.
    """

    def __init__(self, api, **kwargs):
        self.api = api
        self.base_url = f"{self.api.host}/jsonrpc"

    
    def post(self, method: str, params: dict, fmg_type: T = dict()) -> FMGResponse[T]:
        """Sends a POST request to the FortiManager API.

        Args:
            method (str): get, exec, add, set, update, delete.
            params (dict): Payload data to send with the request.
            fmg_type (T): Type of the FMGObject to return, defaults to dict.

        Returns:
            FMGResponse: FMG Response status, message and data.
        """

        headers = {
            "Authorization": f"Bearer {self.api.token}"
        }

        data = {
            "method": method.lower(),
            "verbose": 1 if self.api.verbose else 0,
            "params": [params]
        }

        result = FMGResponse[T]()
        response = requests.post(url=self.base_url, json=data, verify=self.api.verify, headers=headers)

        api_result = {}
        if response.status_code == 200:
            api_result = response.json()["result"][0]
            result.success = True
        else:
            result.success = False

        # handling empty result list
        if not api_result.get("data"):
            result.data = []
        else:
            objects = []
            data = api_result.get("data")
            if isinstance(data, dict):
                objects.append(fmg_type(**data) if not isinstance(fmg_type, dict) else data)
            elif isinstance(data, list):
                for value in data:
                    objects.append(fmg_type(**value) if not isinstance(fmg_type, dict) else value)

            result.data = objects

        result.status = api_result.get("status", {}).get("code", 400)

        if result.status != 0:
            result.message = api_result.get("status", {}).get("message", None)

        return result
    