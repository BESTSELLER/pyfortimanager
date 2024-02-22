from pyfortimanager.core.fortimanager import FortiManager


class FortiSwitches_Proxy(FortiManager):
    """API class for proxy calls to FortiSwitches. Send and receive API calls to/from an online FortiGate.
    """

    def __init__(self, **kwargs):
        super(FortiSwitches_Proxy, self).__init__(**kwargs)

    def all(self, fortigate: str, switch_id: str = None, adom: str = None, timeout: int = None):
        """Retrieves a list of all or a single managed FortiSwitches on the FortiGate.

        Args:
            fortigate (str): Name of the FortiGate.
            switch_id (str, optional): Serial number of a specific FortiSwitch.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.
            timeout (int, optional): How long to wait for the FortiGate to respond. Defaults to the proxy_timeout set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": "/sys/proxy/json",
            "data":
                {
                    "target": [
                        f"/adom/{adom or self.api.adom}/device/{fortigate}"
                    ],
                    "action": "get",
                    "resource": f"/api/v2/monitor/switch-controller/managed-switch/status"
                }
        }

        # Optional fields
        if switch_id:
            params['data']['resource'] += f"?mkey={switch_id}"

        return self.post(method="exec", params=params)

    def authorize(self, switch_id: str, fortigate: str, vdom: str = "root", adom: str = None, timeout: int = None):
        """Authorizes a FortiSwitch on the FortiGate.

        Args:
            switch_id (str): Serial number of the FortiSwitch to authorize.
            fortigate (str): Name of the FortiGate.
            vdom (str): Name of the virtual domain for the FortiGate.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.
            timeout (int, optional): How long to wait for the FortiGate to respond. Defaults to the proxy_timeout set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": "/sys/proxy/json",
            "data":
                {
                    "target": [
                        f"/adom/{adom or self.api.adom}/device/{fortigate}"
                    ],
                    "action": "post",
                    "payload": {
                        "vdom": vdom,
                        "mkey": switch_id,
                        "admin": "enable"
                    },
                    "timeout": timeout or self.api.proxy_timeout,
                    "resource": "/api/v2/monitor/switch-controller/managed-switch/update"
                }
        }

        return self.post(method="exec", params=params)

    def deauthorize(self, switch_id: str, fortigate: str, vdom: str = "root", adom: str = None, timeout: int = None):
        """Deauthorizes a FortiSwitch on the FortiGate.

        Args:
            switch_id (str): Serial number of the FortiSwitch to deauthorize.
            fortigate (str): Name of the FortiGate.
            vdom (str): Name of the virtual domain for the FortiGate.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.
            timeout (int, optional): How long to wait for the FortiGate to respond. Defaults to the proxy_timeout set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": "/sys/proxy/json",
            "data":
                {
                    "target": [
                        f"/adom/{adom or self.api.adom}/device/{fortigate}"
                    ],
                    "action": "post",
                    "payload": {
                        "vdom": vdom,
                        "mkey": switch_id,
                        "admin": "discovered"
                    },
                    "timeout": timeout or self.api.proxy_timeout,
                    "resource": "/api/v2/monitor/switch-controller/managed-switch/update"
                }
        }

        return self.post(method="exec", params=params)

    def restart(self, switch_id: str, fortigate: str, vdom: str = "root", adom: str = None, timeout: int = None):
        """Restarts a FortiSwitch.

        Args:
            switch_id (str): Serial number of the FortiSwitch to restart.
            fortigate (str): Name of the FortiGate.
            vdom (str): Name of the virtual domain for the FortiGate.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.
            timeout (int, optional): How long to wait for the FortiGate to respond. Defaults to the proxy_timeout set when the API was instantiated.

        Returns:
            dict: JSON data.
        """

        params = {
            "url": "/sys/proxy/json",
            "data":
                {
                    "target": [
                        f"/adom/{adom or self.api.adom}/device/{fortigate}"
                    ],
                    "action": "post",
                    "payload": {
                        "vdom": vdom,
                        "mkey": switch_id,
                    },
                    "timeout": timeout or self.api.proxy_timeout,
                    "resource": "/api/v2/monitor/switch-controller/managed-switch/restart"
                }
        }

        return self.post(method="exec", params=params)
