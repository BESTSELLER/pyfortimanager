from pyfortimanager.core.api import BaseModel


class FortiSwitchesProxy(BaseModel):
    """API class for proxy calls to FortiSwitches. Send and receive API calls to/from an online FortiGate.
    """

    def __init__(self, **kwargs):
        super(FortiSwitchesProxy, self).__init__(**kwargs)

    def all(self, fortigate: str, switch_id: str = None, adom: str = None, timeout: int = None):
        """Retrieves a list of all or a single managed FortiSwitches on the FortiGate.

        Args:
            fortigate (str): Name of the FortiGate.
            switch_id (str, optional): Name of a specific FortiSwitch.
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
                    "resource": "/api/v2/monitor/switch-controller/managed-switch/status"
                }
        }

        # Optional fields
        if switch_id:
            params['data']['resource'] += f"?mkey={switch_id}"

        return self.post(method="exec", params=params)

    def authorize(self, switch_id: str, fortigate: str, vdom: str = "root", adom: str = None, timeout: int = None):
        """Authorizes a FortiSwitch on the FortiGate.

        Args:
            switch_id (str): Name of the FortiSwitch to authorize.
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
            switch_id (str): Name of the FortiSwitch to deauthorize.
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
            switch_id (str): Name of the FortiSwitch to restart.
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

    def bounce_port(self, switch_id: str, switch_port: str, fortigate: str, duration: int = 1, adom: str = None, timeout: int = None):
        """Bounce a FortiSwitch port.

        Args:
            switch_id (str): Name of the FortiSwitch to restart.
            switch_port (str): Switch port id
            fortigate (str): Name of the FortiGate.
            duration (int): Duration in seconds for the port to be down
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
                        "duration": duration,
                        "mkey": switch_id,
                        "port": switch_port,
                        "stop": True

                    },
                    "timeout": timeout or self.api.proxy_timeout,
                    "resource": "/api/v2/monitor/switch-controller/managed-switch/bounce-port"
                }
        }

        return self.post(method="exec", params=params)