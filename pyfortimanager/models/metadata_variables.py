from pyfortimanager.core.fortimanager import FortiManager


class MetadataVariables(FortiManager):
    """API class for Metadata Variables in Policy & Objects.
    """

    def __init__(self, **kwargs):
        super(MetadataVariables, self).__init__(**kwargs)

    def all(self, name: str = None, adom: str = None):
        """Retrieves all metadata variables or a single metadata variable with members.

        Args:
            name (str, optional): Name of a specific variable.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/config/adom/{adom or self.api.adom}/obj/fmg/variable",
            "option": [
                "scope member"
            ]
        }

        # Retrieve a single variable
        if name:
            params['url'] += f"/{name}"

        return self.post(method="get", params=params)

    def add(self, name: str, description: str = None, default_value: str = None, revision_note: str = None, adom: str = None):
        """Adds a new metadata variable.

        Args:
            name (str): Name of the new variable.
            description (str, optional): Desceription for the new variable.
            default_value (str, optional): Default value for the new variable.
            revision_note (str, optional): Change note.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/config/adom/{adom or self.api.adom}/obj/fmg/variable",
            "data": {
                "name": name
            }
        }

        # Optional fields
        if default_value:
            params['data']['value'] = default_value

        if description:
            params['data']['description'] = description

        if revision_note:
            params['revision note'] = revision_note

        return self.post(method="add", params=params)

    def update(self, name: str, rename: str = None, description: str = None, default_value: str = None, revision_note: str = None, adom: str = None):
        """Updates a metadata variable.

        Args:
            name (str): Name of the variable to update.
            rename (str, optional): New name of the variable.
            description (str, optional): Desceription for the variable.
            default_value (str, optional): Default value for the variable.
            revision_note (str, optional): Change note.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/config/adom/{adom or self.api.adom}/obj/fmg/variable/{name}",
            "data": {}
        }

        # Optional fields
        if rename:
            params['data']['name'] = rename

        if description:
            params['data']['description'] = description

        if default_value:
            params['data']['value'] = default_value

        if revision_note:
            params['revision note'] = revision_note

        return self.post(method="update", params=params)

    def delete(self, name: str, adom: str = None):
        """Deletes a metadata variable.

        Args:
            name (str): Name of the variable to delete.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/config/adom/{adom or self.api.adom}/obj/fmg/variable/{name}"

        }

        return self.post(method="delete", params=params)

    def add_member(self, variable: str, value: str, fortigate: str, vdom: str = "global", adom: str = None):
        """Adds a FortiGate as a member to a metadata variable.

        Args:
            variable (str): Name of the variable.
            value (str): Value for the variable.
            fortigate (str): Name of the FortiGate to add as a member.
            vdom (str): Name of the virtual domain for the FortiGate.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/config/adom/{adom or self.api.adom}/obj/fmg/variable/{variable}/dynamic_mapping",
            "data": {
                "_scope": {
                    "name": fortigate,
                    "vdom": vdom
                },
                "value": value
            }
        }

        return self.post(method="add", params=params)

    def update_member(self, variable: str, value: str, fortigate: str, vdom: str = "global", adom: str = None):
        """Updates a FortiGate member and its metadata variable.

        Args:
            variable (str): Name of the variable.
            value (str): Value for the variable.
            fortigate (str): Name of the FortiGate member.
            vdom (str): Name of the virtual domain for the FortiGate.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/config/adom/{adom or self.api.adom}/obj/fmg/variable/{variable}/dynamic_mapping",
            "data": {
                "_scope": {
                    "name": fortigate,
                    "vdom": vdom
                },
                "value": value
            }
        }

        return self.post(method="update", params=params)

    def remove_member(self, variable: str, fortigate: str, vdom: str = "global", adom: str = None):
        """Updates a FortiGate member and its metadata variable.

        Args:
            variable (str): Name of the variable.
            fortigate (str): Name of the FortiGate member.
            vdom (str): Name of the virtual domain for the FortiGate.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/config/adom/{adom or self.api.adom}/obj/fmg/variable/{variable}/dynamic_mapping/{fortigate}/{vdom}"
        }

        return self.post(method="delete", params=params)
