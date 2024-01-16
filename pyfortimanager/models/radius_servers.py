from pyfortimanager.core.fortimanager import FortiManager


class RADIUS_Servers(FortiManager):
    """API class for the RADIUS Servers in Policy & Objects.
    """

    def __init__(self, **kwargs):
        super(RADIUS_Servers, self).__init__(**kwargs)

    def all(self, name: str = None, adom: str = None):
        """Retrieves all RADIUS servers or a single RADIUS server.

        Args:
            name (str): Name of the radius server.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/config/adom/{adom or self.api.adom}/obj/user/radius",
        }

        if name:
            params['url'] += f"/{name}"

        return self.post(method="get", params=params)

    def add_member(self, fortigate: str, fortigate_source_ip: str, fortigate_nas_ip: str, radius_server: str, radius_server_ip: str, radius_secret: str, radius_secondary_server_ip: str = None, radius_secondary_secret: str = None, vdom: str = "root", adom: str = None):
        """Adds a FortiGate as a member to a RADIUS server.

        Args:
            radius_server (str): Name of the RADIUS server to add the member to.
            fortigate (str): Name of the FortiGate to add as a member.
            vdom (str): Name of the virtual domain for the FortiGate.
            fortigate_source_ip (str): Source IP for the FortiGate.
            fortigate_nas_ip (str): NAS IP for the FortiGate.
            radius_server_ip (str): IP of the primary RADIUS server.
            radius_secret (str): Secret for the primary RADIUS server.
            radius_secondary_server_ip (str, optional): IP of the secondary RADIUS server.
            radius_secondary_secret (str, optional): Secret for the secondary RADIUS server.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/config/adom/{adom or self.api.adom}/obj/user/radius/{radius_server}/dynamic_mapping",
            "data": {
                "_scope": [
                    {
                        "name": fortigate,
                        "vdom": vdom
                    }
                ],
                "server": radius_server_ip,
                "secret": radius_secret,
                "source-ip": fortigate_source_ip,
                "nas-ip": fortigate_nas_ip
            }
        }

        # Optional fields
        if radius_secondary_server_ip:
            params['data']['secondary-server'] = radius_secondary_server_ip

        if radius_secondary_secret:
            params['data']['secondary-secret'] = radius_secondary_secret

        return self.post(method="add", params=params)

    def update_member(self, radius_server: str, fortigate: str, vdom: str = "root", fortigate_source_ip: str = None, fortigate_nas_ip: str = None, radius_server_ip: str = None, radius_secret: str = None, radius_secondary_server_ip: str = None, radius_secondary_secret: str = None, adom: str = None):
        """Updates a FortiGate member on the RADIUS server.

        Args:
            radius_server (str): Name of the RADIUS server to update the member on.
            fortigate (str): Name of the FortiGate member to update.
            vdom (str): Name of the virtual domain for the FortiGate.
            fortigate_source_ip (str): Source IP for the FortiGate.
            fortigate_nas_ip (str): NAS IP for the FortiGate.
            radius_server_ip (str): IP of the primary RADIUS server.
            radius_secret (str): Secret for the primary RADIUS server.
            radius_secondary_server_ip (str): IP of the secondary RADIUS server.
            radius_secondary_secret (str): Secret for the secondary RADIUS server.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": f"/pm/config/adom/{adom or self.api.adom}/obj/user/radius/{radius_server}/dynamic_mapping",
            "data": {
                "_scope": [
                    {
                        "name": fortigate,
                        "vdom": vdom
                    }
                ]
            }
        }

        # Optional fields
        if radius_server_ip:
            params['data']['server'] = radius_server_ip

        if radius_secret:
            params['data']['secret'] = radius_secret

        if radius_secondary_server_ip:
            params['data']['secondary-server'] = radius_secondary_server_ip

        if radius_secondary_secret:
            params['data']['secondary-secret'] = radius_secondary_secret

        if fortigate_source_ip:
            params['data']['source-ip'] = fortigate_source_ip

        if fortigate_nas_ip:
            params['data']['nas-ip'] = fortigate_nas_ip

        return self.post(method="update", params=params)
