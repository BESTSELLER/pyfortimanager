from pyfortimanager.core.fortimanager import FortiManager


class FortiAPs(FortiManager):
    """API class for FortiAPs.
    """

    def __init__(self, **kwargs):
        super(FortiAPs, self).__init__(**kwargs)

    def all(self, fortigate: str, vdom: str="root", wtp_id: str=None, adom: str=None):
        """Retrieves all FortiAPs or a single FortiAP from a FortiGate.

        Args:
            fortigate (str): Name of the FortiGate.
            vdom (str): Name of the virtual domain for the FortiGate.
            wtp_id (str): Serial number of a specific FortiAP.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/config/adom/{adom or self.api.adom}/obj/wireless-controller/wtp",
            "scope member": [
                {
                    "name": fortigate,
                    "vdom": vdom
                }
            ]
        }

        if wtp_id:
            params['url'] += f"/{wtp_id}"

        return self.post(method="get", params=params)

    def upgrade(self, fortigate: str, wtp_id: str, image: str):
        """Updates the firmware of a specific FortiAP.

        Args:
            fortigate (str): Name of the FortiGate.
            wtp_id (str): Serial number of the FortiAP.
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
                                "id": wtp_id,
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

    def refresh(self, fortigates: list, adom: str=None):
        """Refreshes all FortiAPs from one or more FortiGates.

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
                "ctype": 1,
                "device": fortigates,
                "options": 3,
                "resync": 1
            }
        }

        return self.post(method="exec", params=params)

    def profiles(self, name: str=None, adom: str=None):
        """Retrieves a list of all AP profiles or a single AP profile.

        Args:
            name (str): Name of a specific AP profile.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/config/adom/{adom or self.api.adom}/obj/wireless-controller/wtp-profile"
        }

        if name:
            params['url'] += f"/{name}"

        return self.post(method="get", params=params)

    def add(self, name: str, wtp_id: str, fortigate: str, vdom: str="root", wtp_profile: str=None, prefer_img_ver: str=None, description: str=None, adom: str=None):
        """Adds a new FortiAP.

        Args:
            name (str): Name of the FortiAP.
            wtp_id (str): Serial number of the FortiAP.
            fortigate (str): Name of the FortiGate connected to the FortiSwitch.
            vdom (str): Name of the virtual domain for the FortiGate.
            wtp_profile (str, optional): Name of the AP profile used for this AP.
            prefer_img_ver (str, optional): Enforce the firmware version of the FortiAP. Ex. 7.2.3-b0365.
            description (str, optional): Description of the FortiAP.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/config/adom/{adom or self.api.adom}/obj/wireless-controller/wtp",
            "data": {
                "name": name,
                "wtp-id": wtp_id,
                "_platform-type": 68
            },
            "scope member": [
                {
                    "name": fortigate,
                    "vdom": vdom
                }
            ]
        }

        # Optional fields
        if wtp_profile:
            params['data']['wtp-profile'] = wtp_profile
        
        if prefer_img_ver:
            params['data']['_prefer-img-ver'] = prefer_img_ver

        if description:
            params['data']['location'] = description

        return self.post(method="add", params=params)

    def update(self, wtp_id: str, fortigate: str, vdom: str="root", name: str=None, wtp_profile: str=None, description: str=None, adom: str=None):
        """Updates a FortiAP.

        Args:
            wtp_id (str): Serial number of the FortiAP to update.
            fortigate (str): Name of the FortiGate connected to the FortiSwitch.
            vdom (str): Name of the virtual domain for the FortiGate.
            name (str, optional): Name of the FortiAP.
            wtp_profile (str, optional): Name of the AP profile used for this AP.
            description (str, optional): Description of the FortiAP.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/config/adom/{adom or self.api.adom}/obj/wireless-controller/wtp",
            "data": {
                "wtp-id": wtp_id
            },
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

        if wtp_profile:
            params['data']['wtp_profile'] = wtp_profile

        if description:
            params['data']['location'] = description

        return self.post(method="update", params=params)

    def delete(self, wtp_id: str, fortigate: str, vdom: str="root", adom: str=None):
        """Deletes a FortiAP.

        Args:
            wtp_id (str): Serial number of the FortiAP to delete.
            fortigate (str): Name of the FortiGate connected to the FortiSwitch.
            vdom (str): Name of the virtual domain for the FortiGate.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/config/adom/{adom or self.api.adom}/obj/wireless-controller/wtp/{wtp_id}",
            "scope member": [
                {
                    "name": fortigate,
                    "vdom": vdom
                }
            ]
        }
        
        return self.post(method="delete", params=params)