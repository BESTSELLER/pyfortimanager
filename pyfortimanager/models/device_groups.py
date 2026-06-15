from typing import Optional
from pyfortimanager.core.api import BaseModel
from pyfortimanager.core.filter import FiltersType


class DeviceGroups(BaseModel):
    """API class for Device Groups in the Device Manager.
    """

    def __init__(self, **kwargs):
        super(DeviceGroups, self).__init__(**kwargs)

    def filter(self, filters: FiltersType, adom: str = None, fields: Optional[list[str]] = None):
        """Filters device groups.

        Args:
            filters (FiltersType): Filters to apply.
            adom (str, optional): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.
            fields (Optional[list[str]], optional): Fields to return. Defaults to None.

        Returns:
            _type_: _description_
        """
        params = {
            "filter": filters.generate(),
            "loadsub": 0,
            "url": f"/dvmdb/adom/{adom or self.api.adom}/group",
            "option": [
                "object member"
            ]
        }

        if fields:
            params["fields"] = fields

        result = self.post(method="get", params=params)
        return result

    def all(self, name: str = None, adom: str = None):
        """Retrieves all device groups or a single device group with members.

        Args:
            name (str): Name of a specific device group.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/dvmdb/adom/{adom or self.api.adom}/group",
            "option": [
                "object member"
            ]
        }

        # Retrieve a specific device group
        if name:
            params['url'] += f"/{name}"

        return self.post(method="get", params=params)

    def add(self, name: str, description: str = None, adom: str = None):
        """Adds a device group.

        Args:
            name (str): Name of the device group.
            description (str, optional): Description of the device group.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/dvmdb/adom/{adom or self.api.adom}/group/{name}",
            "data": {
                "name": name,
                "desc": description
            }
        }

        return self.post(method="add", params=params)

    def update(self, name: str, rename: str = None, description: str = None, adom: str = None):
        """Updates a device group.

        Args:
            name (str): Name of the device group to update.
            rename (str, optional): New name of the device group.
            description (str, optional): Description of the device group.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/dvmdb/adom/{adom or self.api.adom}/group/{name}",
            "data": {}
        }

        # Optional fields
        if rename:
            params['data']['name'] = rename

        if description:
            params['data']['desc'] = description

        return self.post(method="update", params=params)

    def delete(self, name: str, adom: str = None):
        """Deletes a device group.

        Args:
            name (str): Name of the device group to delete.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/dvmdb/adom/{adom or self.api.adom}/group/{name}"
        }

        return self.post(method="delete", params=params)

    def add_member(self, name: str, fortigate: str, vdom: str = "root", adom: str = None):
        """Adds a FortiGate as a member to a device group.

        Args:
            name (str): Name of the device group.
            fortigate (str): Name of the FortiGate to add as a member.
            vdom (str): Name of the virtual domain for the FortiGate.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/dvmdb/adom/{adom or self.api.adom}/group/{name}/object member",
            "data": [
                {
                    "name": fortigate,
                    "vdom": vdom
                }
            ]
        }

        return self.post(method="add", params=params)

    def remove_member(self, name: str, fortigate: str, vdom: str = "root", adom: str = None):
        """Removes a FortiGate as a member from a device group.

        Args:
            name (str): Name of the device group.
            fortigate (str): Name of the FortiGate to remove as a member.
            vdom (str): Name of the virtual domain for the FortiGate.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/dvmdb/adom/{adom or self.api.adom}/group/{name}/object member",
            "data": [
                {
                    "name": fortigate,
                    "vdom": vdom
                }
            ]
        }

        return self.post(method="delete", params=params)
