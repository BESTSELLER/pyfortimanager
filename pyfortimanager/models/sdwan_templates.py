from pyfortimanager.core.fortimanager import FortiManager


class SDWAN_Templates(FortiManager):
    """API class for SD-WAN Templates in the Device Manager.
    """

    def __init__(self, **kwargs):
        super(SDWAN_Templates, self).__init__(**kwargs)

    def all(self, name: str = None, adom: str = None):
        """Retrieves all SD-WAN templates or a single SD-WAN template with members.

        Args:
            name (str): Name of the SD-WAN template.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/wanprof/adom/{adom or self.api.adom}"
        }

        # Retrieve a single SD-WAN template
        if name:
            params['url'] += f"/{name}"

        return self.post(method="get", params=params)

    def delete(self, name: str, adom: str = None):
        """Deletes a SD-WAN template.

        Args:
            name (str): Name of the SD-WAN template to delete.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/wanprof/adom/{adom or self.api.adom}/{name}",
            "confirm": 1
        }

        return self.post(method="delete", params=params)

    def add_member(self, name: str, fortigate: str, vdom: str = "root", adom: str = None):
        """Adds a FortiGate as a member to a SD-WAN template.

        Args:
            name (str): Name of the SD-WAN template.
            fortigate (str): Name of the FortiGate to add as a member.
            vdom (str): Name of the virtual domain for the FortiGate.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/wanprof/adom/{adom or self.api.adom}/{name}/scope member",
            "data": [
                {
                    "name": fortigate,
                    "vdom": vdom
                }
            ]
        }

        return self.post(method="add", params=params)

    def remove_member(self, name: str, fortigate: str, vdom: str = "root", adom: str = None):
        """Removes a FortiGate as a member from a SD-WAN template.

        Args:
            name (str): Name of the SD-WAN template.
            fortigate (str): Name of the FortiGate to remove as a member.
            vdom (str): Name of the virtual domain for the FortiGate.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/wanprof/adom/{adom or self.api.adom}/{name}/scope member",
            "data": [
                {
                    "name": fortigate,
                    "vdom": vdom
                }
            ]
        }

        return self.post(method="delete", params=params)
