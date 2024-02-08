from pyfortimanager.core.fortimanager import FortiManager


class FortiSwitches(FortiManager):
    """API class for FortiSwitches.
    """

    def __init__(self, **kwargs):
        super(FortiSwitches, self).__init__(**kwargs)

    def all(self, fortigate: str = None, vdom: str = "root", switch_id: str = None, adom: str = None):
        """Retrieves all FortiSwitches or a single FortiSwitch from a FortiGate.

        Args:
            fortigate (str, optional): Optional name of a specific FortiGate.
            vdom (str): Name of the virtual domain for the FortiGate.
            switch_id (str, optional): Optional serial number of a specific FortiSwitch. Note: FortiGate is required to use this filter.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/config/adom/{adom or self.api.adom}/obj/fsp/managed-switch",
            "scope member": [
                {
                    "name": "All_FortiGate"
                }
            ]
        }

        # Optional fields
        if fortigate:
            params['scope member'][0]['name'] = fortigate
            params['scope member'][0]['vdom'] = vdom

            # To use switch_id, we must provide fortigate aswell.
            if switch_id:
                params['url'] += f"/{switch_id}"

        return self.post(method="get", params=params)

    def upgrade(self, fortigate: str, switch_id: str, image: str):
        """Updates the firmware of a specific FortiSwitch.

        Args:
            fortigate (str): Name of the FortiGate.
            switch_id (str): Serial number of the FortiSwitch.
            image (str): Support version with a build number. e.g., 6.4.12-b2060.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": "/um/image/upgrade/ext",
            "data": {
                "create_task": "enable",
                "devices": [
                    {
                        "controllers": [
                            {
                                "id": switch_id,
                                "image": image
                            }
                        ],
                        "name": fortigate
                    }
                ],
                "flags": 0
            }
        }

        return self.post(method="exec", params=params)

    def refresh(self, fortigates: list, adom: str = None):
        """Refreshes all FortiSwitches from one or more FortiGates.

        Args:
            fortigates (list): List of FortiGate OID's to refresh. Example: [60123, 601234]
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": "/deployment/get/controller/status",
            "data": {
                "adom": adom or self.api.adom,
                "ctype": 4,
                "device": fortigates,
                "options": 3,
                "resync": 1
            }
        }

        return self.post(method="exec", params=params)

    def interfaces(self, switch_id: str, fortigate: str, vdom: str = "root"):
        """Retrives all interfaces on the specified FortiSwitch.

        Args:
            switch_id (str): Serial number of the FortiSwitch.
            fortigate (str): Name of the FortiGate connected to the FortiSwitch.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/config/device/{fortigate}/vdom/{vdom}/switch-controller/managed-switch/{switch_id}"
        }

        return self.post(method="get", params=params)

    def interfaces_update(self, ports: list, switch_id: str, fortigate: str, vdom: str = "root"):
        """Updates all interfaces on the specified FortiSwitch.

        Args:
            ports (list): List with all ports and their configuration.
            switch_id (str): Serial number of the FortiSwitch.
            fortigate (str): Name of the FortiGate connected to the FortiSwitch.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/config/device/{fortigate}/vdom/{vdom}/switch-controller/managed-switch/{switch_id}",
            "data": {
                "ports": ports
            }
        }

        return self.post(method="update", params=params)

    def add_to_adom(self, name: str, platform: str, switch_id: str, fortigate: str, vdom: str = "root", interface: str = "Fortilink", adom: str = None, prefer_img_ver: str = None):
        """Adds a new FortiSwitch as a model device in the FortiSwitch Manager (ADOM).

        Args:
            name (str): Name of the FortiSwitch.
            platform (str): Model name of the FortiSwitch. Ex. FortiSwitch-108E-FPOE.
            switch_id (str): Serial number of the FortiSwitch.
            interface (str): Name of the FortiGate interface connected to the FortiSwitch.
            fortigate (str): Name of the FortiGate connected to the FortiSwitch.
            vdom (str): Name of the virtual domain for the FortiGate.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.
            prefer_img_ver (str, optional): Enforce the firmware version of the FortiSwitch. Ex. 7.2.5-b0453.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/config/adom/{adom or self.api.adom}/obj/fsp/managed-switch",
            "data": {
                "switch-id": switch_id,
                "name": name,
                "state": 2,
                "is-model": 1,
                "platform": platform,
                "vlan-interface": interface
            },
            "scope member": [
                {
                    "name": fortigate,
                    "vdom": vdom
                }
            ]
        }

        # Optional fields
        if prefer_img_ver:
            params['data']['prefer-img-ver'] = prefer_img_ver

        return self.post(method="add", params=params)

    def add_to_fortigate(self, name: str, switch_id: str, fortigate: str, vdom: str = "root", prefer_img_ver: str = None):
        """Adds a new FortiSwitch as a model device on the FortiGate in the FortiSwitch Manager.

        Args:
            name (str): Name of the FortiSwitch.
            switch_id (str): Serial number of the FortiSwitch.
            fortigate (str): Name of the FortiGate connected to the FortiSwitch.
            vdom (str): Name of the virtual domain for the FortiGate.
            prefer_img_ver (str, optional): Enforce the firmware version for the FortiSwitch. Ex. 7.2.5-b0453.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/config/device/{fortigate}/vdom/{vdom}/switch-controller/managed-switch",
            "data": {
                "name": name,
                "switch-id": switch_id,
            }
        }

        # Optional fields
        if prefer_img_ver:
            params['data']['prefer-img-ver'] = prefer_img_ver

        return self.post(method="add", params=params)

    def update_in_adom(self, switch_id: str, fortigate: str, vdom: str = "root", adom: str = None, name: str = None, prefer_img_ver: str = None):
        """Updates a FortiSwitch in the FortiSwitch Manager (ADOM).

        Args:
            switch_id (str): Serial number of the FortiSwitch to update.
            fortigate (str): Name of the FortiGate connected to the FortiSwitch.
            vdom (str): Name of the virtual domain for the FortiGate.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.
            name (str, optional): Name of the FortiSwitch.
            prefer_img_ver (str, optional): Enforce the firmware version for the FortiSwitch. Ex. 7.2.5-b0453.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/config/adom/{adom or self.api.adom}/obj/fsp/managed-switch/{switch_id}",
            "data": {},
            "scope member": [
                {
                    "name": fortigate,
                    "vdom": vdom
                }
            ]
        }

        # Optional fields
        if name:
            params['data']['name'] = name

        if prefer_img_ver:
            params['data']['prefer-img-ver'] = prefer_img_ver

        return self.post(method="update", params=params)

    def update_on_fortigate(self, switch_id: str, fortigate: str, vdom: str = "root", name: str = None, description: str = None):
        """Updates a FortiSwitch on the FortiGate in the FortiSwitch Manager.

        Args:
            switch_id (str): Serial number of the FortiSwitch to update.
            fortigate (str): Name of the FortiGate connected to the FortiSwitch.
            vdom (str): Name of the virtual domain for the FortiGate.
            name (str, optional): Name of the FortiSwitch.
            description (str, optional): Description of the FortiSwitch.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/config/device/{fortigate}/vdom/{vdom}/switch-controller/managed-switch/{switch_id}",
            "data": {}
        }

        # Optional fields
        if name:
            params['data']['name'] = name

        if description:
            params['data']['description'] = description

        return self.post(method="update", params=params)

    def delete_in_adom(self, switch_id: str, fortigate: str, vdom: str = "root", adom: str = None):
        """Updates a FortiSwitch in the FortiSwitch Manager (ADOM).

        Args:
            switch_id (str): Serial number of the FortiSwitch to delete.
            fortigate (str): Name of the FortiGate.
            vdom (str): Name of the virtual domain for the FortiGate.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/config/adom/{adom or self.api.adom}/obj/fsp/managed-switch/{switch_id}",
            "scope member": [
                {
                    "name": fortigate,
                    "vdom": vdom
                }
            ],
        }

        return self.post(method="delete", params=params)

    def delete_on_fortigate(self, switch_id: str, fortigate: str, vdom: str = "root"):
        """Deletes a FortiSwitch on the FortiGate in the FortiSwitch Manager.

        Args:
            switch_id (str): Serial number of the FortiSwitch to delete.
            fortigate (str): Name of the FortiGate.
            vdom (str): Name of the virtual domain for the FortiGate.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/config/device/{fortigate}/vdom/{vdom}/switch-controller/managed-switch/{switch_id}"
        }

        return self.post(method="delete", params=params)
