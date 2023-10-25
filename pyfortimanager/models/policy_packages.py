from pyfortimanager.core.fortimanager import FortiManager


class Policy_Packages(FortiManager):
    """API class for Policy Packages in Policy & Objects.
    """

    def __init__(self, **kwargs):
        super(Policy_Packages, self).__init__(**kwargs)

    def all(self, name: str=None, adom: str=None):
        """Retrieves all policy packages or a single policy package with members.

        Args:
            name (str, optional): Name of a policy package.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/pkg/adom/{adom or self.api.adom}"
        }

        # Retrieve a single policy package
        if name:
            params['url'] += f"/{name}"

        return self.post(method="get", params=params)

    def add_member(self, name: str, fortigate: str, vdom: str="root", adom: str=None):
        """Adds a FortiGate as a member to a policy package.

        Args:
            name (str): Name of the policy package.
            fortigate (str): Name of the FortiGate to be added as a member.
            vdom (str): Name of the virtual domain for the FortiGate.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/pkg/adom/{adom or self.api.adom}/{name}/scope member",
            "data": [
                {
                    "name": fortigate,
                    "vdom": vdom
                }
            ]
        }

        return self.post(method="add", params=params)

    def remove_member(self, name: str, fortigate: str, vdom: str="root", adom: str=None):
        """Removes a FortiGate as a member from a policy package.

        Args:
            name (str): Name of the policy package.
            fortigate (str): Name of the FortiGate to remove as a member.
            vdom (str): Name of the virtual domain for the FortiGate.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/pkg/adom/{adom or self.api.adom}/{name}/scope member",
            "data": [
                {
                    "name": fortigate,
                    "vdom": vdom
                }
            ]
        }

        return self.post(method="delete", params=params)