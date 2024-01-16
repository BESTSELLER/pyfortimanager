from pyfortimanager.core.fortimanager import FortiManager


class CLI_Template_Groups(FortiManager):
    """API class for CLI Template Groups in the Device Manager.
    """

    def __init__(self, **kwargs):
        super(CLI_Template_Groups, self).__init__(**kwargs)

    def all(self, name: str = None, adom: str = None):
        """Retrieves all CLI template groups or a single CLI template group with members.

        Args:
            name (str, optional): Name of a CLI template group.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/config/adom/{adom or self.api.adom}/obj/cli/template-group",
            "option": [
                "scope member"
            ]
        }

        # Retrieve a single CLI template group
        if name:
            params['url'] += f"/{name}"

        return self.post(method="get", params=params)

    def add(self, name: str, members: list = None, description: str = None, adom: str = None):
        """Adds a CLI template group.

        Args:
            name (str): Name of the CLI template group.
            description (str, optional): Description of the CLI template group.
            members (list, optional): List of CLI Templates in the group.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/config/adom/{adom or self.api.adom}/obj/cli/template-group",
            "data": {
                "name": name,
                "member": members,
                "description": description
            }
        }

        return self.post(method="add", params=params)

    def update(self, name: str, members: list = None, description: str = None, adom: str = None):
        """Updates a CLI template group.

        Args:
            name (str): Name of the CLI template group to update.
            description (str, optional): Description of the CLI template group.
            members (list, optional): List of CLI Templates in the group.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/config/adom/{adom or self.api.adom}/obj/cli/template-group",
            "data": {
                "name": name
            }
        }

        # Optional fields
        if members:
            params['data']['member'] = members

        if description:
            params['data']['description'] = description

        return self.post(method="update", params=params)

    def delete(self, name: str, adom: str = None):
        """Deletes a CLI template group.

        Args:
            name (str): Name of the CLI template group to delete.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/config/adom/{adom or self.api.adom}/obj/cli/template-group",
            "confirm": 1,
            "filter": [
                "name",
                "in",
                name
            ],
        }

        return self.post(method="delete", params=params)

    def add_member(self, name: str, fortigate: str, vdom: str = "root", adom: str = None):
        """Adds a FortiGate as a member to a CLI template group.

        Args:
            name (str): Name of the CLI template group.
            fortigate (str): Name of the FortiGate to add as a member.
            vdom (str): Name of the virtual domain for the FortiGate.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/config/adom/{adom or self.api.adom}/obj/cli/template-group/{name}/scope member",
            "data": [
                {
                    "name": fortigate,
                    "vdom": vdom
                }
            ]
        }

        return self.post(method="add", params=params)

    def remove_member(self, name: str, fortigate: str, vdom: str = "root", adom: str = None):
        """Removes a FortiGate as a member from a CLI template group.

        Args:
            name (str): Name of the CLI template group.
            device (str): Name of the FortiGate to remove as a member.
            vdom (str): Name of the virtual domain for the FortiGate.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/config/adom/{adom or self.api.adom}/obj/cli/template-group/{name}/scope member",
            "data": [
                {
                    "name": fortigate,
                    "vdom": vdom
                }
            ]
        }

        return self.post(method="delete", params=params)
