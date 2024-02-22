from pyfortimanager.core.fortimanager import FortiManager


class FortiAPs_Proxy(FortiManager):
    """API class for proxy calls to FortiAPs. Send and receive API calls to/from an online FortiGate.
    """

    def __init__(self, **kwargs):
        super(FortiAPs_Proxy, self).__init__(**kwargs)

    def all(self, fortigate: str, adom: str = None, timeout: int = None):
        """Retrieves a list of managed FortiAPs on the FortiGate.

        Args:
            fortigate (str): Name of the FortiGate.
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
                    "timeout": timeout or self.api.proxy_timeout,
                    "resource": "/api/v2/monitor/wifi/managed_ap"
                }
        }

        return self.post(method="exec", params=params)

    def authorize(self, wtp_id: str, fortigate: str, vdom: str = "root", adom: str = None, timeout: int = None):
        """Authorizes a FortiAP on the FortiGate.

        Args:
            wtp_id (str): Serial number of the FortiAP to authorize.
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
                        "wtpname": wtp_id,
                        "admin": "enable"
                    },
                    "timeout": timeout or self.api.proxy_timeout,
                    "resource": "/api/v2/monitor/wifi/managed_ap/set_status"
                }
        }

        return self.post(method="exec", params=params)

    def deauthorize(self, wtp_id: str, fortigate: str, vdom: str = "root", adom: str = None, timeout: int = None):
        """Deauthorizes a FortiAP on the FortiGate.

        Args:
            wtp_id (str): Serial number of the FortiAP to deauthorize.
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
                        "wtpname": wtp_id,
                        "admin": "discovered"
                    },
                    "timeout": timeout or self.api.proxy_timeout,
                    "resource": "/api/v2/monitor/wifi/managed_ap/set_status"
                }
        }

        return self.post(method="exec", params=params)

    def restart(self, wtp_id: str, fortigate: str, vdom: str = "root", adom: str = None, timeout: int = None):
        """Restarts a FortiAP.

        Args:
            wtp_id (str): Serial number of the FortiAP to restart.
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
                        "wtpname": wtp_id,
                    },
                    "timeout": timeout or self.api.proxy_timeout,
                    "resource": "/api/v2/monitor/wifi/managed_ap/restart"
                }
        }

        return self.post(method="exec", params=params)

    def clients(self, fortigate: str, vdom: str = "root", adom: str = None, timeout: int = None):
        """Retrieves a list of all connected Wi-Fi clients on the FortiGate.

        Args:
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
                    "action": "get",
                    "timeout": timeout or self.api.proxy_timeout,
                    "resource": f"/api/v2/monitor/wifi/client?vdom={vdom}"
                }
        }

        return self.post(method="exec", params=params)
