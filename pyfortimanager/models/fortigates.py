from pyfortimanager.core.fortimanager import FortiManager


class FortiGates(FortiManager):
    """API class for FortiGates.
    """

    def __init__(self, **kwargs):
        super(FortiGates, self).__init__(**kwargs)

    def all(self, fortigate: str = None, adom: str = None):
        """Retrieves all FortiGates or a single FortiGate.

        Args:
            name (str): Name of a specific FortiGate.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/dvmdb/adom/{adom or self.api.adom}/device",
            "option": [
                "get meta"
            ]
        }

        # Retrieve a single FortiGate
        if fortigate:
            params['url'] += f"/{fortigate}"

        return self.post(method="get", params=params)

    def upgrade(self, fortigate: str, image: str, adom: str = None):
        """Upgrades the firmware on the FortiGate.

        Args:
            fortigate (str): Name of the FortiGate.
            image (str): Support version with a build number. e.g., 6.4.12-b2060.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": "/um/image/upgrade/ext",
            "data": {
                "adom": adom or self.api.adom,
                "create_task": "enable",
                "devices": [
                    {
                        "image": image,
                        "name": fortigate
                    }
                ],
                "flags": 0
            }
        }

        return self.post(method="exec", params=params)

    def refresh(self, fortigates: dict, adom: str = None):
        """Refreshes a list of FortiGates.

        Args:
            fortigates (dict): Dict of FortiGate name and OID's to refresh. Ex: { "name": "FortiGate-VM64-1", "oid": "12345" }, { "name": "FortiGate-VM64-2", "oid": "23456" }
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": "/dvm/cmd/update/dev-list",
            "data": {
                "adom": adom or self.api.adom,
                "flags": [
                    "create_task",
                    "nonblocking"
                ],
                "update-dev-member-list": [fortigates]
            }
        }

        return self.post(method="exec", params=params)

    def interfaces(self, fortigate: str, interface: str = None):
        """Retrieves all interfaces or a single interface from a FortiGate.

        Args:
            name (str): Name of the FortiGate.
            interface (str): Name of an interface.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/config/device/{fortigate}/global/system/interface"
        }

        # Retrieve a single interface
        if interface:
            params['url'] = f"/{interface}"

        return self.post(method="get", params=params)

    def add(self, serial: str, mr: int, os_ver: int, name: str = None, mgmt_mode: str = "fmg", os_type: str = "fos", adm_usr: str = None, adm_pass: str = None, description: str = None, meta_fields: dict = None, flags: int = 67371040, prefer_img_ver: str = None, adom: str = None):
        """Adds a new FortiGate as a model device in FortiManager.

        Args:
            name (str): Name of the FortiGate. Default is serial number.
            serial (str): Serial number of the FortiGate.
            mr (int): Minor OS version.
            os_ver (int): Major OS version.
            os_type (str): fos, fsw, foc, fml, faz, fwb, fch, fct, log, fmg, fsa, fdd, fac, fpx, fna, ffw, fsr, fad, fdc, fap, fxt, fts, fai, fwc, fis, fed. Default is fos.
            mgmt_mode (str): unreg, fmg, faz, fmgfaz. Default is fmg.
            flags (int): Various settings in the "Add Device"-dialog in FortiManager. Use FortiManager to retrieve a specific combination. Default is 67371040.
            adm_usr (str, optional): Default admin username.
            adm_pass (str, optional): Default admin password.
            description (str, optional): Description of the FortiGate.
            meta_fields (dict, optional): Meta fields for the FortiGate. Default is fmg.
            prefer_img_ver (str, optional): Enforce the firmware version of the FortiGate. Ex. 7.0.9-b444.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": "/dvm/cmd/add/device",
            "data": {
                "adom": adom or self.api.adom,
                "device": {
                    "flags": flags,
                    "mgmt_mode": mgmt_mode,
                    "mr": mr,
                    "name": name or serial,
                    "os_type": os_type,
                    "os_ver": os_ver,
                    "sn": serial
                }
            }
        }

        # Optional fields
        if adm_usr:
            params['data']['device']['adm_usr'] = adm_usr

        if adm_pass:
            params['data']['device']['adm_pass'] = adm_pass

        if description:
            params['data']['device']['desc'] = description

        if meta_fields:
            params['data']['device']['meta fields'] = meta_fields

        if prefer_img_ver:
            params['data']['device']['prefer_img_ver'] = prefer_img_ver

        return self.post(method="exec", params=params)

    def update(self, fortigate: str, meta_fields: dict = None, adm_pass: str = None, adm_usr: str = None, description: str = None, ip: str = None, latitude: float = None, longitude: float = None, name: str = None, hostname: str = None, prefer_img_ver: str = None, adom: str = None):
        """Updates a FortiGate.

        Args:
            fortigate (str): Name of the FortiGate to update.
            meta_fields (dict): All meta fields in a dict.
            adm_pass (str, optional): Admin password.
            adm_usr (str, optional): Admin username.
            description (str, optional): Description of the FortiGate.
            ip (str, optional): Public IP address of the FortiGate.
            latitude (float, optional): GPS latitude coordinates.
            longitude (float, optional): GPS longitude coordinates.
            name (str, optional): Name of the FortiGate.
            hostname (str, optional): Hostname of the FortiGate.
            prefer_img_ver (str, optional): Enforce the firmware version of the FortiGate. Ex. 7.0.9-b444.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/dvmdb/adom/{adom or self.api.adom}/device/{fortigate}",
            "data": {}
        }

        # Update optional fields
        if adm_pass:
            params['data']['adm_pass'] = adm_pass

        if adm_usr:
            params['data']['adm_usr'] = adm_usr

        if description:
            params['data']['desc'] = description

        if ip:
            params['data']['ip'] = ip

        if latitude:
            params['data']['latitude'] = latitude

        if longitude:
            params['data']['longitude'] = longitude

        if name:
            params['data']['name'] = name

        if hostname:
            params['data']['hostname'] = hostname

        if meta_fields:
            params['data']['meta fields'] = meta_fields

        if prefer_img_ver:
            params['data']['device']['prefer_img_ver'] = prefer_img_ver

        return self.post(method="update", params=params)

    def delete(self, fortigate: str, adom: str = None):
        """Deletes a FortiGate.

        Args:
            fortigate (str): Name of the FortiGate to delete.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": "/dvm/cmd/del/device",
            "data": {
                "adom": adom or self.api.adom,
                "device": fortigate
            }
        }

        return self.post(method="exec", params=params)
