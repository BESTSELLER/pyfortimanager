from pyfortimanager.core.fortimanager import FortiManager


class FortiSwitches(FortiManager):
    """API class for FortiSwitches.
    """

    def __init__(self, **kwargs):
        super(FortiSwitches, self).__init__(**kwargs)

    def all(self, fortigate: str, vdom: str="root", switch_id: str=None, adom: str=None):
        """Retrieves all FortiSwitches or a single FortiSwitch from a FortiGate.

        Args:
            fortigate (str): Name of the FortiGate.
            vdom (str): Name of the virtual domain for the FortiGate.
            switch_id (str, optional): Serial number of a specific FortiSwitch.
            adom (str, optional): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/config/adom/{adom or self.api.adom}/obj/fsp/managed-switch",
            "scope member": [
                {
                    "name": fortigate,
                    "vdom": vdom
                }
            ]
        }

        # Retrieve a single FortiSwitch
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
    
    def refresh(self, fortigates: list):
        """Refreshes all FortiSwitches from a FortiGate.

        Args:
            fortigates (list): List of FortiGate OID's to refresh. Example: [60123, 601234]
    
        Returns:
            dict: JSON data.
        """

        params = {
            "url": "/deployment/get/controller/status",
            "data": {
                "adom": 3,
                "ctype": 4,
                "device": fortigates,
                "options": 3,
                "resync": 1
            }
        }

        return self.post(method="exec", params=params)

    def interfaces(self, switch_id: str, fortigate: str, vdom: str="root"):
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

    def interfaces_update(self, ports: list, switch_id: str, fortigate: str, vdom: str="root"):
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