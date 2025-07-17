from typing import Literal, Optional
from pyfortimanager.core.api import BaseModel
from pyfortimanager.core.filter import FiltersType


class FirewallObjects(BaseModel):
    """API class for Firewall Objects in Policy & Objects.
    """

    def __init__(self, **kwargs):
        super(FirewallObjects, self).__init__(**kwargs)

    def filter(self, type: Literal["address", "addrgrp"], filters: FiltersType, fields: Optional[list[str]] = None, adom: str = None):
        """Retrieves a list of objects based on filters.

        Args:
            filters (FiltersType): filters
            fields (Optional[list[str]], optional): fields. Defaults to all fields.

        Returns:
            FMGResponse[dict]: data
        """
        params = {
            "filter": filters.generate(),
            "loadsub": 0,
            "url": f"/pm/config/adom/{adom or self.api.adom}/obj/firewall/{type}"
        }

        if fields:
            params["fields"] = fields

        result = self.post(method="get", params=params)
        return result

    def add_address(self, name: str, prefix: str, mask: str, type: Literal["address", "wildcard"] = "address", adom: str = None):
        """Adds a firewall address object.

        Args:
            name (str): Name of the address object
            prefix (str): IP address prefix
            mask (str): Subnet mask
            type (str, optional): Type of the address object. Defaults to "address", values: "address", "wildcard".
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/config/adom/{adom or self.api.adom}/obj/firewall/address",
            "data": {
                "name": name,
            }
        }

        if type == "address":
            params['data']['subnet'] = [prefix, mask]
        
        if type == "wildcard":
            params['data']['type'] = "wildcard"
            params['data']['wildcard'] = [prefix, mask]


        return self.post(method="add", params=params)

    def update_address(self, name: str, prefix: str, mask: str, type: Literal["address", "wildcard"] = "address", adom: str = None):
        """Updates a firewall address object.

        Args:
            name (str): Name of the address object
            prefix (str): IP address prefix
            mask (str): Subnet mask
            type (str, optional): Type of the address object. Defaults to "address", values: "address", "wildcard".
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/config/adom/{adom or self.api.adom}/obj/firewall/address",
            "data": {
                "name": name,
            }
        }

        if type == "address":
            params['data']['subnet'] = [prefix, mask]
        
        if type == "wildcard":
            params['data']['type'] = "wildcard"
            params['data']['wildcard'] = [prefix, mask]

        return self.post(method="update", params=params)
    

    def add_address_group(self, name: str, members: list[str], adom: str = None):
        """Adds a firewall address group.

        Args:
            name (str): Name of the address group
            members (list[str]): List of members in the address group
        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/config/adom/{adom or self.api.adom}/obj/firewall/addrgrp",
            "data": {
                "name": name,
                "members": members
            }
        }


        return self.post(method="add", params=params)

    def update_address_group(self, name: str, members: list[str], adom: str = None):
        """Updates a firewall address objgroupect.

        Args:
            name (str): Name of the address group
            members (list[str]): List of members in the address group

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/config/adom/{adom or self.api.adom}/obj/firewall/addrgrp",
            "data": {
                "name": name,
                "members": members
            }
        }

        return self.post(method="update", params=params)