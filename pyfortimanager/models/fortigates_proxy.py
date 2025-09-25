from pyfortimanager.core.api import BaseModel


class FortiGatesProxy(BaseModel):
    """API class for proxy calls to FortiGates. Send and receive API calls to/from an online FortiGate.
    """

    def __init__(self, **kwargs):
        super(FortiGatesProxy, self).__init__(**kwargs)

    def status(self, fortigate: str, adom: str = None, timeout: int = None):
        """Retrieve basic system status on the FortiGate.

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
                    "resource": "/api/v2/monitor/system/status"
                }
        }

        return self.post(method="exec", params=params)

    def resource_usage(self, fortigate: str, adom: str = None, scope: str = "global", resource: str = None, interval: str = None, timeout: int = None):
        """Retrieves current and historical usage data for a provided resource on the FortiGate.

        Args:
            fortigate (str): Name of the FortiGate.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.
            scope (str): Scope from which to retrieve the interface stats from [vdom|global]. Default is global.
            resource (str. optional): Get a specific resource to get usage data for. Defaults to all resources. 
            interval (str, optional): Time interval of resource usage [1-min|10-min|30-min|1-hour|12-hour|24-hour]. Defaults to all intervals.
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
                    "resource": f"/api/v2/monitor/system/resource/usage/?scope={scope}"
                }
        }

        # Optional fields
        if resource:
            params['data']['resource'] += f"&resource={resource}"

        if interval:
            params['data']['resource'] += f"&interval={interval}"

        return self.post(method="exec", params=params)

    def interfaces(self, fortigate: str, adom: str = None, scope: str = "global", include_vlan: bool = True, include_aggregate: bool = True, interface: str = None, timeout: int = None):
        """Retrieves a list of interfaces or a specific interface and their configuration on the FortiGate.

        Args:
            fortigate (str): Name of the FortiGate.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.
            scope (str): Scope from which to retrieve the interface stats from [vdom|global]. Default is global.
            include_vlan (bool): Enable to include VLANs in result list. Default is True.
            include_aggregate (bool): Enable to include Aggregate interfaces in result list. Default is True.
            interface (str, optional): Retrieve this interface only.
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
                    "resource": f"/api/v2/monitor/system/interface/?scope={scope}&include_vlan={include_vlan}&include_aggregate={include_aggregate}"
                }
        }

        # Optional fields
        if interface:
            params['data']['resource'] += f"&interface_name={interface}"

        return self.post(method="exec", params=params)

    def transceivers(self, fortigate: str, adom: str = None, scope: str = "global", timeout: int = None):
        """Retrieves a list of transceivers used on the FortiGate.

        Args:
            fortigate (str): Name of the FortiGate.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.
            scope (str): Scope from which to retrieve the interface stats from [vdom|global]. Default is global.
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
                    "resource": f"/api/v2/monitor/system/interface/transceivers?scope={scope}"
                }
        }

        return self.post(method="exec", params=params)

    def dhcp_leases(self, fortigate: str, adom: str = None, scope: str = "global", ipv6: bool = True, interface: str = None, timeout: int = None):
        """Retrieves a list of all DHCP and DHCPv6 leases on the FortiGate.

        Args:
            fortigate (str): Name of the FortiGate.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.
            scope (str): Scope from which to retrieve the interface stats from [vdom|global]. Default is global.
            ipv6 (bool): Include IPv6 addresses in the response. Default is True.
            interface (str, optional): Retrieve DHCP leases for this interface only.
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
                    "resource": f"/api/v2/monitor/system/dhcp/?scope={scope}&ipv6={ipv6}"
                }
        }

        # Optional fields
        if interface:
            params['data']['resource'] += f"&interface={interface}"

        return self.post(method="exec", params=params)

    def reboot(self, fortigate: str, adom: str = None, timeout: int = None):
        """Reboots a given fortigate

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
                    "action": "post",
                    "timeout": timeout or self.api.proxy_timeout,
                    "resource": "/api/v2/monitor/system/os/reboot"
                }
        }


        return self.post(method="exec", params=params)

    def device_query(self, fortigate: str, adom: str = None, timeout: int = None):
        """Retrieves detected devices from a fortigate

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
                    "resource": "/api/v2/monitor/user/device/query?&with_fortilink=true"
                }
        }

        return self.post(method="exec", params=params)

    def vpn_ipsec(self, fortigate: str, adom: str = None, timeout: int = None):
        """Retrieves ipsec status from a fortiate

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
                    "resource": "/api/v2/monitor/vpn/ipsec?global=1"
                }
        }

        return self.post(method="exec", params=params)

    def sdwan_sla_log(self, fortigate: str, adom: str = None, vdom: str = "*", timeout: int = None):
        """Retrieve the SDWAN SLA log for a specific FortiGate device.

        Args:
            fortigate (str): The name or serial number of the FortiGate device.
            adom (str, optional): The administrative domain of the device. Defaults to None.
            vdom (str, optional): The virtual domain of the device. Defaults to "*".
            timeout (int, optional): The timeout value for the request. Defaults to None.
        Returns:
            dict: The response from the API containing the SLA log information.
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
                    "resource": f"/api/v2/monitor/virtual-wan/sla-log?vdom={vdom}"
                }
        }

        return self.post(method="exec", params=params)

    def sdwan_interface_log(self, fortigate: str, adom: str = None, vdom: str = "*", timeout: int = None):
        """Retrieve the SDWAN interface log for a specific FortiGate device.

        Args:
            fortigate (str): The name or serial number of the FortiGate device.
            adom (str, optional): The administrative domain of the device. Defaults to None.
            vdom (str, optional): The virtual domain of the device. Defaults to "*".
            timeout (int, optional): The timeout value for the request. Defaults to None.
        Returns:
            dict: The response from the API containing the SLA log information.
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
                    "resource": f"/api/v2/monitor/virtual-wan/interface-log?vdom={vdom}"
                }
        }

        return self.post(method="exec", params=params)

    def get_matched_devices(self, fortigate: str, adom: str = None, vdom: str = "*", include_dynamic: bool = True, timeout: int = None):
        """Retrieves a list of matches devices on a given FortiGate.

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
                    "resource": f"/api/v2/monitor/switch-controller/matched-devices?include_dynamic={include_dynamic}&vdom={vdom}"
                }
        }

        return self.post(method="exec", params=params)

    def get_detected_devices(self, fortigate: str, adom: str = None, vdom: str = "*",timeout: int = None):
        """Retrieves a list of detected devices on a given FortiGate.

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
                    "resource": f"/api/v2/monitor/switch-controller/detected-device?vdom={vdom}"
                }
        }

        return self.post(method="exec", params=params)

    def query_logs(self, fortigate: str, adom: str = None, vdom: str = "root", filter: str = "", start: int = 0, rows: int = 500, timeout: int = None):
        """Queries firewall logs of given FortiGate.

        Args:
            fortigate (str): Name of the FortiGate.
            adom (str): Name of the ADOM. Defaults to the ADOM set when the API was instantiated.
            vdom (str): Name of the VDOM. Defaults to "root".
            filter (str): Filter to apply to the logs. Defaults to "".
            start (int): Starting index for the logs. Defaults to 0.
            rows (int): Number of rows to retrieve. Defaults to 500.
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
                    "resource": f"/api/v2/log/memory/traffic/forward?filter={filter}&start={start}&rows={rows}&vdom={vdom}"
                }
        }

        return self.post(method="exec", params=params)