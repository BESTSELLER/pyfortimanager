from pyfortimanager.core.api import BaseModel


class CLITemplates(BaseModel):
    """API class for CLI Template in the Device Manager.
    """

    def __init__(self, **kwargs):
        super(CLITemplates, self).__init__(**kwargs)


    def add(self, name: str, content: str, description: str = None, is_pre_run: bool = False, adom: str = None):
        """Adds a CLI template.

        Args:
            name (str): Name of the CLI template.
            content (str): Content of the CLI template.
            description (str, optional): Description of the CLI template.
            is_pre_run (bool, optional): Whether the template is a pre-run script. Defaults to False.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/config/adom/{adom or self.api.adom}/obj/cli/template",
            "data": {
                "type": 1,
                "provision": 1 if is_pre_run else 0,
                "name": name,
                "script": content,
                "description": description
            }
        }

        return self.post(method="add", params=params)

    def update(self, name: str, content: str,  description: str = None, is_pre_run: bool = False, adom: str = None):
        """Updates a CLI template.

        Args:
            name (str): Name of the CLI template to update.
            content (str): Content of the CLI template.
            description (str, optional): Description of the CLI template.
            is_pre_run (bool, optional): Whether the template is a pre-run script. Defaults to False.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/config/adom/{adom or self.api.adom}/obj/cli/template",
            "data": {
                "type": 1,
                "provision": 1 if is_pre_run else 0,
                "name": name
            }
        }

        # Optional fields
        if content:
            params['data']['script'] = content

        if description:
            params['data']['description'] = description

        return self.post(method="update", params=params)

    def all(self, name: str = None, adom: str = None):
        """Retrieves all CLI template or a single CLI template with members.

        Args:
            name (str, optional): Name of a CLI template.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/config/adom/{adom or self.api.adom}/obj/cli/template",
            "option": [
                "scope member"
            ]
        }

        # Retrieve a single CLI template
        if name:
            params['url'] += f"/{name}"

        return self.post(method="get", params=params)

    def delete(self, name: str, adom: str = None):
        """Deletes a CLI template.

        Args:
            name (str): Name of the CLI template to delete.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/config/adom/{adom or self.api.adom}/obj/cli/template",
            "confirm": 1,
            "filter": [
                "name",
                "in",
                name
            ],
        }

        return self.post(method="delete", params=params)

    def add_member(self, name: str, fortigate: str, vdom: str = "root", adom: str = None):
        """Adds a FortiGate as a member to a CLI template.

        Args:
            name (str): Name of the CLI template.
            fortigate (str): Name of the FortiGate to add as a member.
            vdom (str): Name of the virtual domain for the FortiGate.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/config/adom/{adom or self.api.adom}/obj/cli/template/{name}/scope member",
            "data": [
                {
                    "name": fortigate,
                    "vdom": vdom
                }
            ]
        }

        return self.post(method="add", params=params)

    def remove_member(self, name: str, fortigate: str, vdom: str = "root", adom: str = None):
        """Removes a FortiGate as a member from a CLI template.

        Args:
            name (str): Name of the CLI template.
            device (str): Name of the FortiGate to remove as a member.
            vdom (str): Name of the virtual domain for the FortiGate.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/config/adom/{adom or self.api.adom}/obj/cli/template/{name}/scope member",
            "data": [
                {
                    "name": fortigate,
                    "vdom": vdom
                }
            ]
        }

        return self.post(method="delete", params=params)